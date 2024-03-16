# Fondation du Langage de Programmation Arabe et Traducteur


Ce projet vise à développer un langage de programmation simple en utilisant la syntaxe arabe. L'objectif principal était de construire les fondations du langage, incluant l'interprète, le lexeur et l'analyseur syntaxique. Bien que l'ambition initiale fût de créer un langage de programmation arabe entièrement fonctionnel, capable de mettre en œuvre des algorithmes complexes, l'absence de structures de données avancées, comme les listes, limite actuellement la capacité à implémenter des algorithmes tels que le Jeu de la Vie de Conway. Cependant, le langage est capable d'exécuter des algorithmes de base, y compris, mais sans s'y limiter :

1. Calculatrice simple
2. Simulation d'un jeu de devinettes
3. Calculateur de factorielle
4. Générateur de séquence de Fibonacci
5. Calculateur d'intérêt simple
6. Comptage et sommation
7. Vérificateur de nombres premiers
8. Algorithme de tri basique
....


## Composants du Projet

### 1. Interpréteur

Le module interpréteur (`interpreter.py`) est responsable de l'exécution du code écrit dans le langage de programmation arabe personnalisé. Il interagit avec le lexeur et l'analyseur syntaxique pour tokeniser et analyser le code entrant, respectivement, puis exécute les instructions résultantes.

### 2. Lexeur

Le module lexeur (`lexer.py`) est chargé de tokeniser l'entrée de code arabe dans l'interpréteur. Il décompose le code en tokens individuels, qui sont ensuite passés à l'analyseur syntaxique pour un traitement ultérieur.

### 3. Analyseur Syntaxique

Le module analyseur syntaxique (`parser.py`) est chargé d'analyser les tokens générés par le lexeur. Il examine la structure du code pour déterminer sa correction grammaticale et pour produire un arbre de syntaxe abstraite (AST), représentant la structure du code.

### 4. Traducteur

Le script de traduction (`translator.py`) est conçu pour traduire le code arabe, spécifiquement `test55.arlp` (une mise en œuvre du Jeu de la Vie de Conway en arabe), en code Python équivalent. Ce traducteur spécialisé sert d'outil pour démontrer l'objectif ultime et la direction du projet.

## Ce qui est Supporté dans la Fondation du Langage de Programmation Arabe

Le langage de programmation arabe prend actuellement en charge les fonctionnalités suivantes :


- **Déclaration de Variable :** Permet de déclarer des variables en utilisant des identifiants arabes, facilitant ainsi la compréhension et l'écriture du code pour les locuteurs natifs.
- **Expressions et Opérateurs :** Supporte l'exécution d'opérations arithmétiques et logiques en utilisant des symboles spécifiquement adaptés à la syntaxe arabe.
- **Instruction d'Impression :** Offre la possibilité d'afficher des données sur la console, employant des mots-clés en arabe pour une intégration fluide avec le reste du code.
- **Instruction If :** Permet l'exécution de logique conditionnelle basée sur des conditions formulées en arabe, enrichissant les capacités de contrôle de flux du langage.
- **Instruction While :** Implémente la possibilité de créer des boucles, facilitant l'itération basée sur des conditions spécifiées en arabe, et soutenant ainsi des structures de contrôle essentielles.

## Exemple d'Exécution de l'Interpréteur


Pour exécuter du code écrit dans le langage de programmation arabe à l'aide de l'interpréteur, exécutez le fichier `main.py` avec un fichier de code arabe comme argument :
```sh
python main.py .\test\test1.arpl
```



## Explication du Jeu de la Vie de Conway

Le Jeu de la Vie de Conway est un automate cellulaire classique conçu par le mathématicien John Conway en 1970. Malgré ses règles simples, il présente un comportement complexe et imprévisible. Voici une brève explication de son fonctionnement :

- **Grille :** Le jeu se déroule sur une grille bidimensionnelle de cellules, où chaque cellule peut être soit vivante, soit morte.
- **Règles :** Le jeu progresse en générations, l'état de chaque cellule étant mis à jour à chaque étape en fonction de quatre règles liées au nombre de voisins vivants.
- **Évolution des Motifs :** Différents motifs peuvent émerger et évoluer sur la grille, certains étant statiques, oscillants ou mobiles.
- **Universalité :** Le Jeu de la Vie est Turing complet, ce qui signifie qu'il peut simuler tout algorithme informatique ou même une machine de Turing universelle.

## Exemple d'Exécution du Traducteur

Pour traduire du code arabe en code Python à l'aide du traducteur, suivez ces

 étapes :

```sh
python translator.py test55.arlp
```

### Sortie

```
Round <fonction intégrée round> :
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻ 
◻ ◼ ◼ ◻ ◻ ◻ ◻ ◻ 
◻ ◼ ◼ ◼ ◻ ◻ ◻ ◻ 
◻ ◻ ◼ ◻ ◼ ◼ ◻ ◻ 
◻ ◻ ◻ ◼ ◼ ◼ ◻ ◻ 
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻ ◼ ◼ ◻
◻ ◻ ◻ ◻ ◻ ◼ ◼ ◻

Round <fonction intégrée round> :
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻
◻ ◼ ◻ ◼ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◼ ◻ ◻ ◻
◻ ◼ ◻ ◻ ◻ ◼ ◻ ◻
◻ ◻ ◻ ◼ ◻ ◼ ◻ ◻
◻ ◻ ◻ ◻ ◻ ◻ ◼ ◻
◻ ◻ ◻ ◻ ◻ ◼ ◼ ◻
◻ ◻ ◻ ◻ ◻ ◼ ◼ ◻

Round <fonction intégrée round> :
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◻
◻ ◻ ◼ ◻ ◼ ◻ ◻ ◻
◻ ◻ ◻ ◻ ◻ ◼ ◻ ◻
◻ ◻ ◻ ◻ ◼ ◼ ◼ ◻
◻ ◻ ◻ ◻ ◼ ◻ ◼ ◻
◻ ◻ ◻ ◻ ◻ ◻ ◻ ◼
◻ ◻ ◻ ◻ ◻ ◼ ◼ ◻
```

## Objectifs Futurs

Bien que l'ambition était de développer un langage de programmation arabe à part entière capable de mettre en œuvre des algorithmes complexes comme le Jeu de la Vie, l'accent est actuellement mis sur l'aspect traducteur du projet. Cependant, l'objectif à long terme reste d'étendre les capacités du langage de programmation arabe et de lui permettre de s'attaquer à des tâches de programmation plus avancées.
