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
