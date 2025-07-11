import duckdb

def create_table():
    con = duckdb.connect('spotify.db')
    # Crée la table seulement si elle n'existe pas déjà
    con.execute("""
        CREATE TABLE IF NOT EXISTS merged_tracks (
            id_track VARCHAR,
            name VARCHAR,
            artists VARCHAR,
            album VARCHAR DEFAULT 'Inconnu', -- Colonne album fictive
            release_date VARCHAR,
            release_year INT,
            duration_ms FLOAT,
            danceability FLOAT,
            id_artist VARCHAR,
            name_artist VARCHAR,
            genres VARCHAR,
            popularity FLOAT
        );
    """)
    con.close()
    print("✅ Table merged_tracks vérifiée/créée")

def insert_data(df):
    con = duckdb.connect("spotify.db")

    # Si la colonne 'album' n’existe pas dans df, la créer avec valeur par défaut
    if 'album' not in df.columns:
        df['album'] = "Inconnu"

    # Supprimer la table existante pour éviter les conflits
    con.execute("DROP TABLE IF EXISTS merged_tracks")

    # Créer la table automatiquement depuis df (schéma identique)
    con.execute("CREATE TABLE merged_tracks AS SELECT * FROM df")

    con.close()
    print("✅ Table merged_tracks créée et données insérées")

def query_data(years, artists, albums):
    con = duckdb.connect('spotify.db')
    
    # Si aucun filtre sélectionné, retourner toutes les données
    if not years and not artists and not albums:
        df = con.execute("SELECT * FROM merged_tracks").fetchdf()
        con.close()
        return df

    # Sinon, appliquer les filtres sélectionnés
    query = "SELECT * FROM merged_tracks WHERE 1=1"
    params = []

    if years:
        query += f" AND release_year IN ({','.join(['?']*len(years))})"
        params += years
    if artists:
        query += f" AND name_artist IN ({','.join(['?']*len(artists))})"
        params += artists
    if albums:
        query += f" AND album IN ({','.join(['?']*len(albums))})"
        params += albums

    df = con.execute(query, params).fetchdf()
    con.close()
    return df