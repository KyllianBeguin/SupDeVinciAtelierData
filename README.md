![Bannière du repo](./media/Banner_repo.png)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Static Badge](https://img.shields.io/badge/Apache%20Superset-green?style=for-the-badge) ![Jupyter](https://img.shields.io/badge/jupyter-F37626.svg?style=for-the-badge&logo=jupyter&logoColor=white)

## Sommaire
1. [Infrastructure](#infrastructure)
    1. [Mise en place](#mise-en-place)
2. [Ateliers](#ateliers)
    1. [Bachelor](#atelier-bachelor)
    2. [Mastère](#atelier-mastère)
3. [Autre](#autre)

## Infrastructure
### Mise en place
1. Disposer d'une machine virtuelle  
    - De préférence, opter pour une machine hébergée chez un cloud provider.  
    - Cette VM servira pour les parties traitement de données / visualisation / machine learning. Vous devez vous assurer de disposer d'assez de ressources
    - Exemple : [D4s_v3 de chez Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/dv4-dsv4-series)
2. S'assurer d'avoir Docker installé
    - [DOC - Comment installer Docker sur Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - [DOC - Post-installation de Docker](https://docs.docker.com/engine/install/linux-postinstall/)
3. Aller dans le dossier `/DataEngineering`
4. Lancer la partie Data Engineering : `docker compose up --build -d`
5. Créer un environnement virtuel Python : `python3 -m venv venv`
    - Installer venv : `pip install virtualenv`
6. Activer l'environnement virtuel : `source venv/bin/activate`
7. Installer les dépendances : `pip install -r requirements.txt`
8. Lancer le flux de traitement de données : `python3 etl.py`
    - *Des logs apparaissent pour vous informer de l'activité du script*
    - La base de données est prête. Elle est consultable ici : `<IP-de-ma-VM>:8080` (mot de passe : `supdevinci` ; base : `atelierdata`)
9. Aller à la racine du projet
10. Lancer la commande `bash get_superset_repo.sh`
    - *Cela créer un dossier `DataViz`*
11. Aller dans le dossier `DataViz`
12. Lancer la commande `docker compose -f docker-compose-non-dev.yml up -d`
13. Aller sur la page web `<IP-de-ma-VM>:8088` et connectez-vous (utilisateur : `admin` ; mot de passe : `admin`)
14. Connecter la base de données mysql à Superset
    - Par défaut, le nom d'utilisateur de la base est `root` et le mot de passe est `supdevinci`
    - Le port est celui par défaut : `3306`
    - L'hôte est : `127.0.0.1`
    - La base est : `atelierdata`
    - Le nom d'utilisateur est : `root`
15. Initier des dashboards et les sauvegarder
    - Il s'agit de coquilles vides qui seront à alimenter par les étudiants.
16. Aller dans le dossier `/MachineLearning`
17. Lancer la commande `docker compose up --build -d`
18. S'assurer que l'ip de hôte de la base est bien celle de votre VM
    - Pour connaître l'ip de votre VM, tapez : `ip a`. Cela devrait vous proposer des ip, à tester.
19. **Félicitation, votre atelier Data peut commencer !**

## Ateliers
### Atelier Bachelor
Objectif : **Comprendre les données de comptages de vélo et piétons à Rennes**  
Durée : 5 à 10 min  
Déroulé de l'atelier : cf [la feuille de route Bachelor](./FeuilleDeRouteBachelor.md)

### Atelier Mastère
Objectifs :  
1. **Rétablir un flux de traitement de données**  
2. Prédire des données  
3. Visualiser les données prédites  

Durée : 20 min  
Déroulé de l'atelier : cf [la feuille de route Mastère](./FeuilleDeRouteMastere.md)  

## Autre
### Schématisation de l'infrastructure retenue
![](./media/AtelierDataTechno.png)
