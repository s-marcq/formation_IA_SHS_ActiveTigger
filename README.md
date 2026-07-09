# Corpus de presse féminine française (1901–1913)

Corpus pour une démo d'annotation et de classification automatique (ActiveTigger) :
étude historique de la presse féminine française de la Belle Époque, en français
courant et lisible (contrairement à la presse du XVIIIe / début XIXe siècle, à
l'orthographe et au style plus difficiles d'accès).

## Sources

Textes OCR en accès libre sur [Internet Archive](https://archive.org), tous entre
1900 et 1935 :

| Journal | Date | Identifiant archive.org |
|---|---|---|
| Femina | 1er mars 1901 | `femina1-3` |
| Femina | 15 octobre 1908 | `femina186-1908` |
| Journal des dames et des modes | 9 numéros, janvier–mars 1913 | `journal-des-dames-et-des-modes-*-1913` |

## Contenu du dossier

- `corpus_txt/` — un fichier `.txt` par volume/numéro (texte OCR nettoyé), nommé
  `Journal_Titre_Date_identifiant.txt`.
- `telecharger_presse_feminine.py` — script qui a téléchargé et nettoyé ces `.txt`
  depuis archive.org (à relancer uniquement si vous voulez régénérer `corpus_txt/`).
- `decoupage_corpus.ipynb` — notebook qui découpe ces textes en extraits de 500
  caractères (sans jamais couper une phrase), puis produit deux fichiers CSV
  (colonnes `text`, `file_name`) :
  - `corpus_annotation.csv` (750 extraits) — à importer dans ActiveTigger pour
    l'annotation et l'entraînement du classifieur ;
  - `corpus_inference.csv` (250 extraits) — mis de côté pour tester le classifieur
    une fois entraîné, jamais vu pendant l'annotation.
- `corpus_annotation_pre_annote_200.csv` — les 200 premiers extraits de
  `corpus_annotation.csv`, déjà annotés (colonne `label`) selon le schéma
  ci-dessous, pour aller plus vite en formation (base indicative : à faire
  contester/corriger par les participants).
- `requirements.txt` — dépendances Python, pour exécuter le notebook sur
  [Binder](https://mybinder.org) sans installation locale.

Les deux CSV de `decoupage_corpus.ipynb` sont déjà fournis dans ce dossier (tirage
reproductible, graine 42), à partir de 1384 extraits disponibles au total ; relancez
simplement le notebook si vous voulez d'autres tailles ou une autre valeur de
`TAILLE_MAX`.

## Piste d'annotation retenue : Éditorial / Publicité

- **Éditorial** — contenu produit par la rédaction : mode, chroniques, critiques,
  fiction, annonces internes au journal (conférences, sommaires, abonnements).
- **Publicité** — réclame commerciale tierce : marque, prix, adresse, mode d'achat
  (cosmétiques, corsets, phonographes, remèdes...).

Ce schéma binaire a été préféré à deux alternatives explorées puis écartées :
- un schéma à 4 classes (Prescriptif/normatif, Descriptif/factuel, Fiction/récit,
  Chronique/commentaire) — plus riche thématiquement, mais bien plus subjectif à
  trancher (plusieurs cas limites en pratique) ;
- un axe « types de femmes » (portraits d'archétypes féminins comme « l'aventurière »
  ou « la jeune fille américaine ») — historiquement le plus intéressant, mais trop
  rare (7 % des extraits sur un échantillon de 200) pour servir de base fiable à un
  exercice d'annotation.

Répartition mesurée sur les 200 premiers extraits : 173 Éditorial (86,5 %) /
27 Publicité (13,5 %). Le déséquilibre est réel mais nettement moins problématique
que celui de l'axe « types de femmes », et le critère de décision (marque + prix +
adresse) est beaucoup plus objectif d'un annotateur à l'autre.

## Notes

- Les textes sont dans le domaine public ; l'OCR provient de scans Google Books ou de
  bibliothèques partenaires d'Internet Archive et contient donc le bruit habituel de
  ce type de numérisation ancienne (publicités, mentions légales, artefacts d'OCR).
- Un item initialement repéré sous le titre « Femina » (1909, identifiant
  `femina0000unse`) s'est révélé être un texte médical en anglais sans rapport avec
  le magazine ; il a été écarté du corpus.
