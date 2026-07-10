# Corpus de presse féminine française (1901–1913)

Corpus pour une démo d'annotation et de classification automatique avec ActiveTigger [1]
sur de la presse féminine française de la Belle Époque, en français
courant.



## Sources

Textes OCR en accès libre sur [Internet Archive](https://archive.org), tous entre
1900 et 1913 :

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
- `corpus_annotation_pre_annote_300.csv` — les mêmes 750 lignes que
  `corpus_annotation.csv`, avec une colonne `label` en plus : les 300 premières
  lignes sont déjà annotées selon le schéma ci-dessous (pour aller plus vite en
  formation — base indicative, à faire contester/corriger par les participants),
  les 450 suivantes ont un `label` vide, à annoter en séance.
- `GUIDE_ANNOTATION.md` — guide de décision Éditorial/Publicité à donner aux
  annotateurs (marqueurs, exemples, cas piégeux).
- `prompt_classification_llm.txt` — prompt prêt à l'emploi pour faire classer les
  extraits par un LLM (mêmes critères que le guide d'annotation).
- `comparaison_generatif_bert.ipynb` — notebook qui compare les performances d'un
  modèle génératif (LLM) et d'un modèle BERT (ActiveTigger) sur le jeu de test,
  à partir de deux exports déposés dans `results/` (voir ci-dessous).
- `results/` — dossier attendu par `comparaison_generatif_bert.ipynb` : déposez-y
  `generations.csv` (export des réponses du LLM) et `predictions_BERT.csv` (export
  ActiveTigger des prédictions BERT). Le notebook y écrit aussi son tableau
  d'évaluation final (`comparaison_generatif_bert.csv`).
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


Répartition mesurée sur les 300 premiers extraits : 251 Éditorial (83,7 %) /
49 Publicité (16,3 %). Le déséquilibre est réel mais le critère de décision (marque + prix +
adresse) est beaucoup plus objectif d'un annotateur à l'autre.


[1] Boelaert J., Ollion É., Schultz É. (2026). ActiveTigger (Version 0.9.9) [Computer software]. https://github.com/activetigger/activetigger

URL docs : https://docs.numerique.gouv.fr/docs/43b2b2bb-266b-4f50-8d01-6c39d554e1fa/
