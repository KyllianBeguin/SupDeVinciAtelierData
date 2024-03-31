# Feuille de route Mastère
## Initalisation
1. Avoir réalisé l'étape de mise en place
    * [DOC - mise en place de l'atelier](https://github.com/KyllianBeguin/SupDeVinciAtelierData?tab=readme-ov-file#mise-en-place)
3. Avec le PC n°1
    1. Se connecter à la machine virtuelle
    2. Aller dans le dossier `./DataEngineering`
    3. Activer l'environnement virtuel : `source venv/bin/activate`
    4. Ouvrir le ficher `etl.py`
4.  Avec le PC n°2
    1. Aller sur `<IP-de-ma-VM>:8888`
    2. Se connecter au serveur jupyter avec le token `my-token`
    3. Aller dans le dossier `/work`
    4. Ouvrir le fichier `labML.ipynb`
  
## Feuille de route
### Partie Data Engineering
1. Placer les étudiants sur le PC n°1
2. Présenter l'objectif : **Rétablir un flux de traitement de données**
    * 💡 Conseil : avec `adminer`, montrer les données actuellement en base
3. Montrer la partie de code a traiter
    * 🚨 Attention : assurez-vous que les étudiants connaissent à minima la bibliothèque Python [pandas](https://pandas.pydata.org/), voire celle utilisé [polars](https://pola.rs/)
4. Faire ajouter les bouts de code par les étudiants
    * Une colonne `heure`
    * Suppression des `counts` *NULL*
    * 💡 Conseil : les étudiants peuvent proposer leurs propres améliorations, en accord avec la partie Machine Learning

### Partie Machine Learning
todo Clément
