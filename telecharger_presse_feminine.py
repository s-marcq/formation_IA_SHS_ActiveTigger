"""
Téléchargement de presse féminine française (XIXe - début XXe siècle) depuis
Internet Archive (archive.org), indépendant de Gallica/BnF.

Titres retenus (tous entre 1900 et 1935, pour un français plus lisible que la presse
du XVIIIe / début XIXe siècle) :
  - Femina (1901, 1908)
  - Journal des dames et des modes (numéros de 1913)

Ce script :
  1. télécharge le texte OCR brut (« _djvu.txt ») de chaque volume/numéro listé
     dans ITEMS, via l'API d'Internet Archive (metadata puis download) ;
  2. nettoie ce texte : suppression de l'en-tête légal Google Books (le cas
     échéant) et du bruit de type « Digitized by ... » laissé par l'OCR sur les
     scans Google ;
  3. enregistre CHAQUE volume/numéro dans un fichier .txt séparé, dans le dossier
     DOSSIER_SORTIE, avec le journal et la date dans le nom du fichier
     (ex. "Journal_des_demoiselles_1833_....txt").

Les fichiers déjà présents dans DOSSIER_SORTIE ne sont pas retéléchargés.

La segmentation en extraits et la constitution des jeux d'annotation/inférence
sont prises en charge séparément par le notebook "decoupage_corpus.ipynb", qui
lit les .txt produits ici.

Usage :
    python telecharger_presse_feminine.py
"""

import os
import re

import requests

# ---------------------------------------------------------------------------
# Paramètres à adapter
# ---------------------------------------------------------------------------

# Items Internet Archive retenus : (identifiant, titre du journal, date)
ITEMS = [
    ("femina1-3", "Femina", "1901-03-01"),
    ("femina186-1908", "Femina", "1908-10-15"),
    ("journal-des-dames-et-des-modes-n.-22-1-gennaio-1913", "Journal des dames et des modes", "1913-01-01"),
    ("journal-des-dames-et-des-modes-n.23-10-gennaio-1913", "Journal des dames et des modes", "1913-01-10"),
    ("journal-des-dames-et-des-modes-20-gennaio-1913", "Journal des dames et des modes", "1913-01-20"),
    ("journal-des-dames-et-des-modes-1-febbraio-1913", "Journal des dames et des modes", "1913-02-01"),
    ("journal-des-dames-et-des-modes-10-febbraio-1913", "Journal des dames et des modes", "1913-02-10"),
    ("journal-des-dames-et-des-modes-20-febbraio-1913", "Journal des dames et des modes", "1913-02-20"),
    ("journal-des-dames-et-des-modes-1-marzo-1913", "Journal des dames et des modes", "1913-03-01"),
    ("journal-des-dames-et-des-modes-10-marzo-1913", "Journal des dames et des modes", "1913-03-10"),
    ("journal-des-dames-et-des-modes-20-marzo-1913", "Journal des dames et des modes", "1913-03-20"),
]

# Dossier de sortie des fichiers .txt (créé automatiquement s'il n'existe pas)
DOSSIER_SORTIE = "corpus_txt"

# Réseau
TIMEOUT = 30

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}


# ---------------------------------------------------------------------------
# Téléchargement depuis Internet Archive
# ---------------------------------------------------------------------------

def obtenir_nom_fichier_texte(identifiant):
    """
    Interroge l'API metadata d'archive.org pour trouver le nom exact du fichier
    texte brut (« ..._djvu.txt ») associé à un item (ce nom ne correspond pas
    toujours à l'identifiant de l'item). Retourne None si aucun fichier de ce
    type n'est trouvé.
    """
    url = f"https://archive.org/metadata/{identifiant}"
    try:
        reponse = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"    [ERREUR RESEAU] Metadata pour '{identifiant}' : {e}")
        return None

    try:
        donnees = reponse.json()
    except ValueError as e:
        print(f"    [ERREUR] Réponse metadata invalide pour '{identifiant}' : {e}")
        return None

    for fichier in donnees.get("files", []):
        nom = fichier.get("name", "")
        if nom.endswith("_djvu.txt"):
            return nom

    return None


def telecharger_texte_archive_org(identifiant):
    """Télécharge le texte OCR brut d'un item Internet Archive. Retourne str ou None."""
    nom_fichier_texte = obtenir_nom_fichier_texte(identifiant)
    if not nom_fichier_texte:
        print(f"    -> Aucun fichier texte brut trouvé pour '{identifiant}'.")
        return None

    url = f"https://archive.org/download/{identifiant}/{requests.utils.quote(nom_fichier_texte)}"
    try:
        reponse = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"    [ERREUR RESEAU] Téléchargement texte pour '{identifiant}' : {e}")
        return None

    texte = reponse.text
    if not texte or len(texte.strip()) < 200:
        return None

    return texte


def nom_fichier_sortie(titre_journal, date_str, identifiant):
    """Construit un nom de fichier .txt lisible et sûr, avec le journal et la date."""
    base = f"{titre_journal}_{date_str}_{identifiant}"
    base = re.sub(r'[\\/*?:"<>|]', "", base)
    base = re.sub(r"\s+", "_", base.strip())
    return base + ".txt"


# ---------------------------------------------------------------------------
# Nettoyage du texte OCR
# ---------------------------------------------------------------------------

def retirer_entete_google_books(texte):
    """
    Retire l'en-tête légal en anglais que Google Books ajoute au début des
    fichiers texte issus de ses propres scans (repérable par sa première phrase,
    toujours identique). Ne fait rien si ce marqueur n'est pas trouvé (item non
    scanné par Google).
    """
    if "This is a digital copy of a book" not in texte[:300]:
        return texte

    for marqueur in ("Book Search helps readers", "google . com", "google.com", "books.google"):
        idx = texte.find(marqueur)
        if idx != -1:
            idx_fin_paragraphe = texte.find("\n\n", idx)
            if idx_fin_paragraphe != -1:
                return texte[idx_fin_paragraphe:]

    return texte


def retirer_bruit_ocr_google(texte):
    """
    Retire le filigrane « Digitized by ... » que l'OCR laisse sur chaque page scannée
    par Google (le mot qui suit "by", en général "Google" mal océrisé, est parfois
    séparé par un retour à la ligne plutôt qu'une simple espace).
    """
    return re.sub(r"Digitized\s*by\s*\S*", " ", texte)


def nettoyer_texte(texte):
    texte = retirer_entete_google_books(texte)
    texte = retirer_bruit_ocr_google(texte)
    return texte


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def main():
    os.makedirs(DOSSIER_SORTIE, exist_ok=True)
    compteur = 0

    for identifiant, titre_journal, date_str in ITEMS:
        chemin_fichier = os.path.join(DOSSIER_SORTIE, nom_fichier_sortie(titre_journal, date_str, identifiant))

        if os.path.exists(chemin_fichier):
            print(f"'{os.path.basename(chemin_fichier)}' déjà présent, on passe au suivant.")
            compteur += 1
            continue

        print(f"Téléchargement de '{titre_journal}' ({date_str}, {identifiant}) ...")

        try:
            texte_brut = telecharger_texte_archive_org(identifiant)
        except Exception as e:
            print(f"  [ERREUR] Téléchargement inattendu, item ignoré : {e}")
            continue

        if not texte_brut:
            print("  -> Texte indisponible, item ignoré.")
            continue

        texte_propre = nettoyer_texte(texte_brut)

        try:
            with open(chemin_fichier, "w", encoding="utf-8") as f:
                f.write(texte_propre)
        except OSError as e:
            print(f"  [ERREUR] Écriture du fichier '{chemin_fichier}' impossible : {e}")
            continue

        compteur += 1
        print(f"  -> Enregistré : {chemin_fichier}")

    print(f"\nTotal : {compteur} fichier(s) .txt disponible(s) dans '{DOSSIER_SORTIE}/'.")


if __name__ == "__main__":
    main()
