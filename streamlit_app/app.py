import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# PAGE CONFIG

st.set_page_config(
    page_title="AMC Music Clustering Dashboard",
    layout="centered"
)

st.title("🎧 AMC Music Clustering Dashboard")
st.write("Explore song clusters based on audio features")

# LOAD DATA

@st.cache_data
def load_data():
    return pd.read_csv(r"D:\WORKOUTS\DATA_CLEANING\Dataset CSV\single_genre_artists.csv")  # keep CSV near app.py

df_amc = load_data()

# Add cluster column if missing

cluster_features = [col for col in [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
] if col in df_amc.columns]

if not cluster_features:
    st.error("❌ None of the clustering features exist in the CSV!")
    st.stop()

if 'cluster' not in df_amc.columns:
    kmeans = KMeans(n_clusters=4, random_state=42)  # change n_clusters as needed
    df_amc['cluster'] = kmeans.fit_predict(df_amc[cluster_features])

# RECOMMENDATION SYSTEM

def recommend_songs(song_name, df, top_n=5):

    if "cluster" not in df.columns:
        st.error("❌ Cluster column not created yet")
        return pd.DataFrame()

    song_row = df[df["name_song"] == song_name]

    if song_row.empty:
        st.error("❌ Song not found")
        return pd.DataFrame()

    cluster = song_row["cluster"].values[0]

    recommendations = (
        df[df["cluster"] == cluster]
        .sort_values("popularity_songs", ascending=False)
        .head(top_n)
    )

    return recommendations

st.markdown("---")
st.subheader("🎶 Song Recommendation")

song_selected = st.selectbox(
    "Select a song",
    df_amc["name_song"].unique()
)

top_n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Recommend Similar Songs"):
    recs = recommend_songs(song_selected, df_amc, top_n)

    st.success("Recommended songs from the same cluster:")
    st.dataframe(
        recs[["name_song", "name_artists", "popularity_songs"]]
    )

st.write(df_amc.columns)

# Add cluster column if missing

cluster_features = [col for col in [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
] if col in df_amc.columns]

if not cluster_features:
    st.error("❌ None of the clustering features exist in the CSV!")
    st.stop()

if 'cluster' not in df_amc.columns:
    kmeans = KMeans(n_clusters=4, random_state=42)  # change n_clusters as needed
    df_amc['cluster'] = kmeans.fit_predict(df_amc[cluster_features])

# SAFETY CHECK

required_cols = ['cluster', 'tempo', 'popularity_songs']
for col in required_cols:
    if col not in df_amc.columns:
        st.error(f"❌ Missing column: {col}")
        st.stop()

# SIDEBAR FILTER

st.sidebar.header("🎚 Filter Options")

cluster_selected = st.sidebar.selectbox(
    "Select Cluster",
    sorted(df_amc['cluster'].unique())
)

# FEATURES (MATCH NOTEBOOK)

features = [
    'duration_ms',       # minutes (converted in notebook)
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
]

cluster_data = df_amc[df_amc['cluster'] == cluster_selected]

# CLUSTER OVERVIEW

st.subheader(f"📌 Cluster {cluster_selected} Overview")
st.caption("Note: Duration is in **minutes**, not milliseconds")
st.dataframe(cluster_data[features].describe().T)

# TOP TRACKS

st.subheader("🔥 Top Tracks in This Cluster")

top_tracks = (
    cluster_data
    .sort_values(by='popularity_songs', ascending=False)
    .head(10)
)

st.dataframe(
    top_tracks[['name_song', 'name_artists', 'popularity_songs']]
)

# SONG RECOMMENDATION SYSTEM

st.subheader("🎶 Recommend Similar Songs")

song = st.selectbox(
    "Select a song",
    df_amc["name_song"].unique(),
    key="song_recommend_selectbox"
)


if st.button("Recommend Similar Songs", key="recommend_button"):
    recs = recommend_songs(song, df_amc)

    st.success("Here are some similar songs you may like:")
    st.dataframe(
        recs[['name_song', 'name_artists', 'popularity_songs']]
    )


# TEMPO DISTRIBUTION

st.subheader("🎵 Tempo Distribution")

fig, ax = plt.subplots()
ax.hist(cluster_data['tempo'], bins=20)
ax.set_xlabel("Tempo (BPM)")
ax.set_ylabel("Count")
st.pyplot(fig)
plt.close(fig)  # 🔴 IMPORTANT FIX

# CLUSTER SUMMARY

st.subheader("📊 Cluster-wise Feature Summary")

cluster_summary = df_amc.groupby('cluster')[features].mean().round(2)
st.dataframe(cluster_summary)

# DOWNLOAD OPTION

st.subheader("⬇ Download Clustered Dataset")

st.download_button(
    label="Download CSV",
    data=df_amc.to_csv(index=False),
    file_name="amc_music_with_clusters.csv",
    mime="text/csv"
)

# FOOTER

st.markdown("---")
st.caption("AMC Music Clustering Dashboard • PCA + KMeans")

