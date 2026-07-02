# Notes sur la Programmation Orientée Objet (POO)

## 1. Qu'est-ce que `self` ?

Le mot-clé `self` représente l'instance actuelle de la classe. Il permet d'accéder aux attributs et aux méthodes de l'objet. En Python, `self` doit toujours être le premier paramètre des méthodes d'instance.

Exemple :

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Ici, `self.name` est un attribut appartenant à chaque objet créé.

---

## 2. Différence entre un attribut public et `_attribut`

Un attribut public est accessible directement depuis l'extérieur de la classe :

```python
student.name
```

Un attribut précédé d'un underscore (`_`) est considéré comme privé par convention :

```python
self._records
```

Cela signifie qu'il ne devrait être utilisé qu'à l'intérieur de la classe ou de ses sous-classes.

---

## 3. Relation avec Laravel Eloquent

En Laravel, les modèles Eloquent encapsulent des données et des comportements.

Exemple :

```php
class User extends Model
```

En Python, nous utilisons également l'héritage :

```python
class CsvDataset(Dataset)
```

La classe enfant hérite des attributs et méthodes de la classe parent et peut ajouter de nouvelles fonctionnalités.

---

## 4. Pourquoi utiliser la POO en Data Science ?

La programmation orientée objet permet d'organiser le code, de le rendre réutilisable et plus facile à maintenir. Elle facilite également la création de pipelines de traitement de données complexes.
