# Manual Tests - Jour 3

## Objectif

Ce document contient les tests manuels réalisés pour vérifier le bon fonctionnement des fonctions du module `src/utils.py`.

| Fonction                           | Entrée                     | Résultat attendu                                                                  | OK ? |
| ---------------------------------- | -------------------------- | --------------------------------------------------------------------------------- | ---- |
| `load_csv("data/sample.csv")`      | `data/sample.csv`          | Retourner une liste de 10 dictionnaires                                           |  oui  |
| `filter_by_min_score(records, 10)` | `records` + `min_score=10` | Retourner 7 enregistrements                                                       | oui     |
| `filter_by_min_score(records, 12)` | `records` + `min_score=12` | Retourner 6 enregistrements                                                       | oui    |
| `average_score(records)`           | `records`                  | Retourner `12.8`                                                                  | oui    |
| `average_score([])`                | `[]`                       | Retourner `0.0`                                                                   |oui     |
| `summarize(records)`               | `records`                  | Retourner `{'count': 10, 'avg_score': 12.8, 'max_score': 18.0, 'min_score': 7.0}` | oui     |

## Résumé des tests

Tous les tests ont été exécutés avec succès. Les fonctions du module `utils.py` retournent les résultats attendus et gèrent correctement les cas particuliers, notamment le cas d'une liste vide dans la fonction `average_score()`. Le script `main.py` s'exécute sans erreur et affiche les statistiques correctes du fichier `sample.csv`.
