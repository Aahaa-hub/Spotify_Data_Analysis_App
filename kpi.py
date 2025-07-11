import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Couleurs Spotify
spotify_green = "#1DB954"
spotify_black = "#191414"

def get_kpis(df):
    """Affiche les indicateurs Spotify et toutes les visualisations."""

    # 🎧 KPI
    st.subheader("🎧 Indicateurs Spotify")
    st.metric("Nombre total de morceaux", df.shape[0])
    avg_duration = df['duration_ms'].mean() / 60000
    st.metric("Durée moyenne (min)", f"{avg_duration:.2f}")

    # 📈 Répartition des morceaux par année
    st.subheader("📈 Répartition des morceaux par année")
    year_counts = df['release_year'].value_counts().sort_index()
    st.line_chart(year_counts)

    # 🎵 Top 10 Chansons de l'année
    st.subheader(f"Top 10 Chansons de l'année {int(df['release_year'].max())}")
    popularity_cols = [col for col in df.columns if 'popularity' in col]
    name_cols = [col for col in df.columns if 'name' in col]

    if popularity_cols and name_cols:
        popularity_col = popularity_cols[0]
        name_col = name_cols[0]
        recent_songs = (
            df[df['release_year'] == df['release_year'].max()]
            .nlargest(10, popularity_col)[[name_col, popularity_col]]
            .sort_values(by=popularity_col, ascending=True)
        )
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(recent_songs[name_col], recent_songs[popularity_col], color=spotify_green)
        ax.set_xlabel("Popularité", color=spotify_black)
        ax.set_title("Top 10 Chansons", color=spotify_black)
        ax.tick_params(axis='x', colors=spotify_black)
        ax.tick_params(axis='y', colors=spotify_black)
        fig.patch.set_facecolor('white')
        plt.tight_layout()
        st.pyplot(fig)
        
    # ⏱️ Distribution de la Durée des Morceaux
    st.subheader("⏱️ Distribution de la Durée des Morceaux")
    durations = df['duration_ms'] / 60000
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(durations, bins=30, color=spotify_green, edgecolor='black')
    ax.set_xlabel("Durée (minutes)", color=spotify_black)
    ax.set_ylabel("Nombre de morceaux", color=spotify_black)
    ax.set_title("Distribution de la Durée des Morceaux Spotify", color=spotify_black)
    ax.tick_params(axis='x', colors=spotify_black)
    ax.tick_params(axis='y', colors=spotify_black)
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    st.pyplot(fig)

    # 🎤 Top 10 Artistes les plus prolifiques
    st.subheader("🎤 Top 10 Artistes les plus prolifiques")
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

    top_artists = df['artists_clean'].dropna().value_counts().head(10)
    if not top_artists.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        top_artists_sorted = top_artists.sort_values(ascending=True)
        ax.barh(top_artists_sorted.index, top_artists_sorted.values, color=spotify_green)
        ax.set_xlabel("Nombre de morceaux", color=spotify_black)
        ax.set_title("Top 10 Artistes les plus prolifiques", color=spotify_black)
        ax.tick_params(axis='x', colors=spotify_black)
        ax.tick_params(axis='y', colors=spotify_black)
        fig.patch.set_facecolor('white')
        plt.tight_layout()
        st.pyplot(fig)