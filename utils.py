import pandas as pd

def load_and_merge_data_from_folder(tracks_path, artists_path):
    tracks_df = pd.read_csv(tracks_path)
    artists_df = pd.read_csv(artists_path)
    
    tracks_df['release_year'] = pd.to_datetime(tracks_df['release_date'], errors='coerce').dt.year
    tracks_df = tracks_df.dropna(subset=['release_year'])
    
    merged_df = pd.merge(
        tracks_df,
        artists_df,
        left_on='artists',
        right_on='id',
        suffixes=('_track', '_artist'),
        how='left'
    )
    return merged_df