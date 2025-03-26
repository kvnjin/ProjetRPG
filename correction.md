# Analyse des infractions aux principes SOLID et Clean Code

## Infractions aux principes SOLID

### Single Responsibility Principle (SRP)
- La classe `Character` gère à la fois la création du personnage, la sélection de la classe et l'affichage des informations
- La classe `CharacterMoove` gère à la fois le déplacement et l'interface utilisateur (affichage des commandes et lecture des entrées)
- La classe `Map` gère à la fois la génération de la carte et son affichage

### Open/Closed Principle (OCP)
- La fonction `getClassStats` est ouverte à la modification pour ajouter de nouvelles classes
- La méthode `move` de `CharacterMoove` est ouverte à la modification pour ajouter de nouvelles directions

### Liskov Substitution Principle (LSP)
- Pas d'héritage utilisé, donc pas d'infraction directe

### Interface Segregation Principle (ISP)
- Pas d'interfaces utilisées, donc pas d'infraction directe

### Dependency Inversion Principle (DIP)
- Les classes dépendent directement de leurs implémentations concrètes plutôt que d'abstractions
- La classe `Character` dépend directement de `characterClass` et `inventory`

## Infractions aux principes Clean Code

### Noms de variables et méthodes
- Utilisation de noms non descriptifs : `x`, `y`, `map`, `room`
- Incohérence dans la casse : mélange de camelCase et snake_case
- Noms de variables en français et en anglais mélangés

### Structure du code
- Méthodes trop longues et complexes
- Duplication de code dans la gestion des directions dans `CharacterMoove`
- Manque de validation des entrées utilisateur
- Manque de gestion des erreurs
