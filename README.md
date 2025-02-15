# Bitcoin Dashboard

Ce projet est une application web interactive développée avec **Dash** et **Plotly** permettant la visualisation du cours du Bitcoin en chandeliers avec des options de filtrage et un mode clair/sombre.

## 📂 Architecture du projet
```
📦 bitcoin_dashboard
├── 📂 assets
│   ├── style.css                
├── 📂 data
│   ├── Btc_Perp_USD.csv         
├── 📂 components
│   ├── __init__.py              
│   ├── layout.py                
│   ├── callbacks.py          
├── app.py                     
├── requirements.txt              
├── README.md                     
```

## Installation & Exécution

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/votre-utilisateur/bitcoin-dashboard.git
cd bitcoin-dashboard
```

### 2️⃣ **Créer un environnement virtuel et l'activer**
```bash
python -m venv venv
source venv/bin/activate  
```

### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Lancer l'application**
```bash
python app.py
```

##  Fonctionnalités
✔️ Affichage du graphique en chandeliers japonnais interactif  
✔️ Filtrage par intervalle temporel (1 minute, 30 minutes, 1 heure, 1 jour)  
✔️ Sélection du type de moyenne mobile (SMA, EMA)   
✔️ Sélection d'une plage de dates personnalisée  
✔️ Mode clair/sombre pour une meilleure lisibilité   

##  Technologies utilisées
- **Dash** (Framework pour applications web interactives en Python)
- **Plotly** (Visualisation de données)
- **Pandas** (Manipulation des données)
- **Bootstrap** (Stylisation de l'interface)

##  Dépannage
Si l'importation des fichiers `layout.py` ou `callbacks.py` échoue, assurez-vous que :
- Le fichier `__init__.py` est bien présent dans `components/`
- Vous lancez le script depuis le bon répertoire racine
- Vous pouvez forcer l'ajout du chemin dans `app.py` en ajoutant ceci au début :
  ```python
  import sys
  import os
  sys.path.append(os.path.abspath(os.path.dirname(__file__)))
  ```