# Corpus de presse féminine française (1774–1833)

Corpus pour une démo d'annotation et de classification automatique (ActiveTigger) :
étude historique de la presse féminine française, de la fin du XVIIIe siècle à la
monarchie de Juillet.

## Sources

Textes OCR en accès libre sur [Internet Archive](https://archive.org), tous
antérieurs à 1850 :

| Journal | Année | Identifiant archive.org |
|---|---|---|
| Journal des dames | 1774 | `journaldesdames00mont` |
| Journal des dames | 1775 | `montanclos-journal-des-dames-janvier-1775` |
| Journal des dames | 1798 | `17584881618888bsb-10919475` |
| Journal des dames et des modes | 1817 | `journal-des-dames-et-des-modes.-1798-1837-vingt-unieme-annee.-1817.` |
| Journal des demoiselles | 1833 | `journaldesdemoi26unkngoog` |

## Contenu du dossier

- `corpus_txt/` — un fichier `.txt` par volume/numéro (texte OCR nettoyé), nommé
  `Journal_Titre_Année_identifiant.txt`.
- `telecharger_presse_feminine.py` — script qui a téléchargé et nettoyé ces `.txt`
  depuis archive.org (à relancer uniquement si vous voulez régénérer `corpus_txt/`).
- `decoupage_corpus.ipynb` — notebook qui découpe ces textes en extraits de 500
  caractères (sans jamais couper une phrase), puis produit deux fichiers CSV
  (colonnes `text`, `file_name`) :
  - `corpus_annotation.csv` (750 extraits) — à importer dans ActiveTigger pour
    l'annotation et l'entraînement du classifieur ;
  - `corpus_inference.csv` (250 extraits) — mis de côté pour tester le classifieur
    une fois entraîné, jamais vu pendant l'annotation.

Les deux CSV sont déjà fournis dans ce dossier (tirage reproductible, graine 42) ;
relancez simplement le notebook si vous voulez d'autres tailles ou une autre valeur
de `TAILLE_MAX`.

## Piste d'annotation proposée (3 classes)

- **Prescriptif / normatif** — le texte prescrit un comportement, une vertu, un rôle
  attendu de la femme.
- **Descriptif / factuel** — constat sans injonction (mode décrite sans jugement,
  recette, actualité, annonce).
- **Fiction / récit** — contes, nouvelles, poésie.

## Notes

- Les textes sont dans le domaine public ; l'OCR provient de scans Google Books ou de
  bibliothèques partenaires d'Internet Archive et contient donc le bruit habituel de
  ce type de numérisation ancienne.
