import streamlit as st
import os
from utils import load_and_merge_data_from_folder
from db import create_table, insert_data, query_data
from kpi import get_kpis

st.cache_data.clear()
st.cache_resource.clear()

st.set_page_config(page_title="Spotify Data Explorer", layout="wide")
st.title("Spotify Data Explorer")

data_folder = "./data"
tracks_file = os.path.join(data_folder, "tracks.csv")
artists_file = os.path.join(data_folder, "artists.csv")


if os.path.exists(tracks_file) and os.path.exists(artists_file):
    df = load_and_merge_data_from_folder(tracks_file, artists_file)
    create_table()
    insert_data(df)

    # Créer la colonne 'artists_clean' UNE SEULE FOIS
    if 'artists_clean' not in df.columns:
        df['artists_clean'] = (
            df['artists']
            .astype(str)
            .str.strip("[]")
            .str.replace("'", "")
            .str.split(",")
            .str[0]
            .str.strip()
        )

    # Dashboard (KPI + Visualisations)
    st.subheader("📊 Aperçu des données fusionnées")
    st.dataframe(df.head())

    years = st.multiselect("Filtrer par année de sortie", sorted(df['release_year'].unique()))
    artists = st.multiselect("Filtrer par artiste", df['name_artist'].dropna().unique())
    albums = st.multiselect("Filtrer par album", df['album'].unique())

    filtered_data = query_data(years, artists, albums)
    st.write(f"{filtered_data.shape[0]} morceaux affichés")
    get_kpis(filtered_data)

    # Téléchargement
    st.subheader("📥 Télécharger les Données")
    st.download_button(
        label="Télécharger les données complètes",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='spotify_full_data.csv',
        mime='text/csv'
    )
else:
    st.warning("Veuillez déposer les fichiers 'tracks.csv' et 'artists.csv' dans le dossier 'data' du projet.")
