Scripts d'Automatisation Système

Ce dépôt contient un ensemble de scripts Python conçus pour automatiser diverses tâches système. Les scripts incluent des fonctionnalités pour importer des données utilisateur dans une base de données, analyser les journaux d'authentification et sauvegarder les fichiers de données.

Aperçu des Scripts

main.py : Le script principal qui orchestre l'exécution des autres scripts. Il appelle séquentiellement des fonctions pour importer des données utilisateur dans une base de données, analyser les journaux d'authentification et sauvegarder les fichiers de données.

csv_to_db.py : Ce script se connecte à une base de données SQLite, crée une table 'users' et la remplit avec des données provenant d'un fichier CSV. La table inclut des colonnes pour l'ID utilisateur, le nom d'utilisateur, l'email, les tentatives de connexion et la date de dernière connexion.

log_analyzer.py : Ce script utilise des expressions régulières pour analyser le fichier 'auth.log'. Il extrait les horodatages, les noms d'utilisateur et les adresses IP des lignes indiquant des tentatives de connexion échouées et affiche ces informations dans une chaîne formatée.

backup.py : Ce script crée une archive horodatée du répertoire 'system_automation/src/'. Il génère un fichier ZIP nommé avec la date actuelle dans le répertoire 'system_automation/src/archive/' et affiche un message de confirmation.

Fichiers de Données

users.csv : Un fichier CSV contenant des enregistrements utilisateur avec des détails incluant l'ID utilisateur, le nom d'utilisateur, l'email, les tentatives de connexion et la date de dernière connexion.

auth.log : Un fichier de journal contenant des tentatives de connexion SSH à un serveur, incluant des tentatives de mot de passe réussies et échouées.

Utilisation

Pour utiliser ces scripts, suivez ces étapes :

Assurez-vous d'avoir Python installé sur votre système.

Clonez ce dépôt sur votre machine locale.

Installez les dépendances requises (le cas échéant) en exécutant :

pip install -r requirements.txt

Exécutez le script principal :

python main.py


Auteurs

Nolan Deruelle, Précieux Juste Bitemo, Éric Kim
