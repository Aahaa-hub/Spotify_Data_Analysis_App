# 🎧 Spotify Data Analysis App

## 📝 Description du projet

Application web interactive permettant d’explorer les données Spotify.  
Elle offre des filtres dynamiques, des visualisations avancées et une analyse complète des morceaux et artistes Spotify.

---

## 🚀 Pour commencer

Cloner ce projet et récupérer les fichiers de données (Git LFS requis) :
```bash
git lfs install 
git clone https://github.com/Aahaa-hub/Spotify_Data_Analysis_App.git
cd Spotify_Data_Analysis_App
git lfs pull
```
📋 Pré-requis
Installer les dépendances nécessaires :
```bash
pip install -r requirements.txt
```
▶️ Démarrage
Lancer l’application :
```bash
streamlit run app.py
or
python -m streamlit run app.py
```

## 📊 Exemples de visualisations générées
- KPI : Nombre total de morceaux, durée moyenne.

- Répartition des morceaux par année (Line Chart).

- Top 10 des chansons populaires (Bar Chart).

- Distribution des durées des morceaux (Histogramme).

- Top 10 des artistes les plus prolifiques (Bar Chart).

- Clustering K-Means (Scatter Plot) des morceaux.
## ⚙️ Technologies utilisées

- **Python**
- **Streamlit**
- **DuckDB**
- **Pandas**
- **Matplotlib**
- **Scikit-Learn**
- **Git LFS** (pour la gestion des fichiers CSV volumineux)

## 🚨 Remarques importantes
- Les fichiers CSV sont inclus dans /data/ et gérés via Git LFS.
- La base DuckDB (spotify.db) est générée automatiquement au lancement.
- L’application est prête à l’emploi immédiatement après installation.

## ✅ Résumé
Une application complète, intuitive et immédiatement exploitable pour explorer les données Spotify.

