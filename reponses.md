# Réponses TP GitHub Actions

## Étape 1
 Création du repository GitHub `mlops-github-actions-tp`.

## Étape 2
Clonage du repository sur ma machine locale avec `git clone`.

## Étape 3
Création du dossier `.github/workflows/`.
>  Ce répertoire contient tous les fichiers YAML qui définissent les workflows GitHub Actions. C’est là que GitHub va chercher automatiquement les automatisations à exécuter.

## Étape 4
Création de `model.py` avec une fonction de prédiction simple.
Création de `test_model.py` pour tester cette fonction avec `pytest`.

## Étape 5
 Création du fichier `requirements.txt` pour installer `pytest`.

## Étape 6
Création du premier workflow `.github/workflows/hello.yml`.

## Étape 7
Commit et push de tous les fichiers.

## Étape 8
Je constate que le workflow **"Hello World"** s’est exécuté automatiquement dans l’onglet **Actions** sur GitHub.

## Étape 9
Création du workflow `.github/workflows/test.yml` pour exécuter les tests automatiquement avec `pytest`.

## Étape 10
Je constate que les **tests se lancent automatiquement** à chaque `push` ou `pull_request`, et qu’ils passent .

## Étape 11 : Introduction d'un bug

🛠 J'ai volontairement modifié la ligne de retour `"positive"` en `"positif"` dans la fonction `predict_sentiment()` du fichier `model.py`.

🔍 Résultat :
Lors du push, le workflow **"Run Tests"** a échoué. Dans l'onglet **Actions**, j'ai constaté que le test `test_predict_positive()` ne passait plus.

 Ce comportement est attendu et montre que l'intégration continue fonctionne bien pour détecter les régressions.

---

## Étape 12 : Correction du bug

 J'ai rétabli le retour `"positive"` dans la fonction `predict_sentiment()`.

Après un nouveau commit/push, le workflow **"Run Tests"** s’est exécuté et **tous les tests sont repassés au vert**.

---

## Étape 13 : Ajout d'une matrice de versions Python

 J’ai modifié le fichier `.github/workflows/test.yml` pour exécuter les tests sur les versions Python suivantes : `3.8`, `3.9`, `3.10`.

Cela permet de s'assurer que mon code fonctionne sur plusieurs environnements.

---

## Étape 14 : Observation des résultats

 Après le push, j’ai constaté dans l’onglet **Actions** que le workflow "Run Tests" s’est exécuté **trois fois en parallèle**, une fois pour chaque version Python définie dans la matrice.

 Très utile pour la compatibilité multiplateforme !

 ## Étape 15 : Création du workflow de lint

J’ai ajouté un nouveau workflow `.github/workflows/lint.yml` utilisant `flake8` pour vérifier le style du code Python.

---

## Étape 16 : Vérification et correction du style

 J’ai ajouté un docstring à la fonction `predict_sentiment()` pour respecter les bonnes pratiques et passer le lint.

 Résultat : dans l’onglet **Actions**, le workflow **"Lint Code"** s’exécute correctement et valide que le style est conforme .

## Étape 17 : Commentaire automatique sur Pull Request

 J’ai créé un workflow `.github/workflows/pr-comment.yml` qui ajoute automatiquement un commentaire à chaque nouvelle Pull Request.

Après avoir ouvert une PR, j’ai constaté qu’un message est automatiquement posté :  
> " Thanks for the PR! The automated tests will run shortly."

 Cela permet de donner du feedback immédiat et d’informer que les tests sont en cours d’exécution.

## Étape 18 : Test du workflow de commentaire automatique

J’ai créé une nouvelle branche `test-pr-comment`, ajouté une modification, puis ouvert une Pull Request vers `main`.

 Résultat : un commentaire automatique est apparu dans la PR avec le message :
> " Thanks for the PR! The automated tests will run shortly."

 Cela confirme que le workflow `pr-comment.yml` fonctionne correctement dès qu’une PR est ouverte.

 ## Étape 19 : Génération d’un badge de statut de build

 J’ai créé un workflow `.github/workflows/badge.yml` qui s’exécute sur chaque push vers `main`.

J’ai ajouté le badge de statut dans le fichier `README.md` :

```markdown
![Build Status](https://github.com/Boubanda/mlops-github-actions-tp/actions/workflows/badge.yml/badge.svg)

