# Guide d'annotation — Éditorial vs Publicité

Corpus de presse féminine française (*Femina*, 1901 et 1908 ; *Journal des dames et
des modes*, 1913). Chaque extrait fait environ 500 caractères et provient d'un OCR
ancien : attendez-vous à des mots mal reconnus, des caractères parasites, des sauts
de mise en page. Ne laissez pas le bruit OCR vous empêcher de juger le **contenu**.

## Principe général

Pour chaque extrait, une seule question : **qui parle, et dans quel but ?**

- **Éditorial** : le texte est produit par la rédaction du journal — article, mode,
  chronique, critique, fiction, ou annonce concernant le journal lui-même
  (abonnements, conférences, concours, sommaires).
- **Publicité** : le texte est une réclame commerciale pour un produit ou service
  d'un tiers (marque de cosmétique, corsetier, horloger, banque, phonographe...).

## Marqueurs à chercher

**Signes de Publicité** (au moins un présent = Publicité) :
- un nom de marque ou de commerçant mis en avant (« EAU MONO », « Corsets Cadolle »,
  « Madame Bellanger »...)
- un prix (« 250 fr. », « Prix du bec complet : 10 fr. »)
- une adresse, un numéro de téléphone, une instruction pour commander
  (« S'adresser à... », « Envoi franco contre 3 fr. », « En vente partout »)
- un mode d'emploi de produit (« Prendre une soucoupe... y ajouter... »)

**Signes d'Éditorial** :
- une description de mode **sans** marque/prix/adresse (page mode du journal —
  souvent avec crédit de créateur : « Boué Sœurs », « Vincent Lachartroulle »)
- un récit, un dialogue, une chronique, une critique de théâtre ou d'art
- une annonce concernant une activité du journal lui-même (le Conservatoire
  *Femina-Musica*, ses conférences, ses concours, ses conditions d'abonnement)

## Exemples tirés du corpus

**Publicité**
> « Élégante robe de visite en drap bleu meunier... 250 fr. [...] 2, rue du
> Pont-Neuf, PARIS [...] Envoi franco de Catalogues et d'Échantillons sur demande »
→ prix + adresse + « envoi franco » = boutique tierce, malgré la description mode.

> « Après un lavage rapide avec l'EAU MONO, on séchera. Mettre deux couches du LAIT
> MONO... »
→ marque + mode d'emploi.

**Éditorial**
> « La jupe, disposée en bande, se rattache par une série de petites boucles de
> strass... (Vincent Lachartroulle) »
→ page mode du journal, créateur crédité, aucune adresse/prix de vente.

> « Rien de plus passionnant pour Alcippe que les aventures. Déjà, il se voit en
> bonne fortune... »
→ récit/fiction.

> « Le prix de l'abonnement est fixé à 100 francs par an pour la France... »
→ ceci concerne l'abonnement **au journal lui-même**, pas un produit tiers : Éditorial.

## Cas piégeux

- **Annonces du journal sur ses propres activités** (conservatoire, conférences,
  concours, abonnement) → **Éditorial**, même si le ton est promotionnel : ce n'est
  pas une réclame pour un tiers.
- **Publicité déguisée en essai** (ex. un texte qui commence par une réflexion
  philosophique — « Quel est donc le dernier prodige du génie humain ? » — avant de
  révéler qu'il s'agit d'un phonographe de marque) → regardez si l'extrait fait
  partie d'une séquence publicitaire plus large (même page, même sujet qui revient
  avec marque/prix un peu plus loin). Si oui → **Publicité**, même si ce passage
  précis n'a pas encore de prix.
- **Liste de noms + réclame sur la même ligne** (ex. sommaire suivi d'une pub
  compressée par l'OCR) → classez selon ce qui domine l'extrait en longueur.
- **Texte trop dégradé par l'OCR pour trancher** → cherchez le nom de fichier
  source ou le contexte des extraits voisins ; à défaut, choisissez Éditorial par
  défaut (c'est la classe majoritaire, l'erreur y coûte moins cher pour
  l'entraînement).

## Répartition attendue

Sur les 300 premiers extraits déjà annotés (voir
`corpus_annotation_pre_annote_300.csv`) : **83,7 % Éditorial / 16,3 % Publicité**.
Un déséquilibre de cet ordre est normal — ne cherchez pas à forcer un équilibre en
reclassant des cas ambigus.
