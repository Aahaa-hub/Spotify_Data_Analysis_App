import streamlit as st
import pandas as pd
from kpi import get_kpis

st.set_page_config(page_title="Spotify Data Explorer - KPI et Top 10 Chansons", layout="wide")
st.title("🎧 Spotify KPI & Top 10 Chansons")

# Chargement des données (CSV ou Parquet selon ton format)
tracks_file = "data/tracks.csv"

if tracks_file.endswith('.csv'):
    df = pd.read_csv(tracks_file)
else:
    df = pd.read_parquet(tracks_file)

# Affichage des KPI + Top 10 Chansons (grâce à la fonction de ton kpi.py)
get_kpis(df)