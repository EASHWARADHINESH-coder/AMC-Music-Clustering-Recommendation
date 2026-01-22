import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AMC Music Clustering Dashboard",
    layout="centered"
)

st.title("🎧 AMC Music Clustering Dashboard")
st.write("Explore song clusters based on audio features")

# ---------------- CSV UPLOAD ----------------

st.subheader("📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload the CSV file (Amazon Music dataset)",
    type="csv"
)

if uploaded_file is None:
    st.warning("Please upload the CSV file to proceed.")
    st.stop()

df_amc = pd.read_csv(uploaded_file)
st.success("CSV loaded successfully!")

# ---------------- REQUIRED COLUMNS CHECK ----------------

required_columns = [
    'name_song', 'name_artists', 'popularity_songs',
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo'
]

missing_cols = [col for col in required_columns if col not in df_amc.columns]

if missing_cols:
    st.error(f"❌ Missing required columns: {missing_cols}")
    st.stop()

# ---------------- CLUSTER FEATURES ----------------

cluster_features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo'
]

# ---------------- APPLY KMEANS ----------------

@st.cache_data
def apply_kmeans(data, features, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data = data.copy()
    data['cluster'] = kmeans.fit_predict(data[features])
    return data

df_amc = apply_kmeans(df_amc, cluster_features)

# ---------------- SIDEBAR ----------------

st.sidebar.header("🎚 Filter Options")

cluster_selected = st.sidebar.selectbox(
    "Select Cluster",
    sorted(df_amc['cluster'].unique())
)

cluster_data = df_amc[df_amc['cluster'] == cluster_selected]

# ---------------- CLUSTER OVERVIEW ----------------

st.subheader(f"📌 Cluster {cluster_selected} Overview")

st.dataframe(
    cluster_data[cluster_features].describe().T.round(2)
)

# ---------------- TOP TRACKS ----------------

st.subheader("🔥 Top Tracks in This Cluster")

top_tracks = (
    cluster_data
    .sort_values(by="popularity_songs", ascending=False)
    .head(10)
)

st.dataframe(
    top_tracks[['name_song', 'name_artists', 'popularity_songs']]
)

# ---------------- RECOMMENDATION SYSTEM ----------------

def recommend_songs(song_name, df, top_n=5):
    song_row = df[df['name_song'] == song_name]

    if song_row.empty:
        return pd.DataFrame()

    cluster = song_row['cluster'].values[0]

    recommendations = (
        df[df['cluster'] == cluster]
        .sort_values(by='popularity_songs', ascending=False)
        .head(top_n)
    )

    return recommendations

st.subheader("🎶 Recommend Similar Songs")

song_selected = st.selectbox(
    "Select a song",
    df_amc['name_song'].unique()
)

top_n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Recommend"):
    recs = recommend_songs(song_selected, df_amc, top_n)

    if recs.empty:
        st.error("Song not found!")
    else:
        st.success("Recommended songs:")
        st.dataframe(
            recs[['name_song', 'name_artists', 'popularity_songs']]
        )

# ---------------- TEMPO DISTRIBUTION ----------------

st.subheader("🎵 Tempo Distribution")

fig, ax = plt.subplots()
ax.hist(cluster_data['tempo'], bins=20)
ax.set_xlabel("Tempo (BPM)")
ax.set_ylabel("Count")
st.pyplot(fig)
plt.close(fig)

# ---------------- CLUSTER SUMMARY ----------------

st.subheader("📊 Cluster-wise Feature Summary")

cluster_summary = (
    df_amc
    .groupby('cluster')[cluster_features]
    .mean()
    .round(2)
)

st.dataframe(cluster_summary)

# ---------------- DOWNLOAD ----------------

st.subheader("⬇ Download Clustered Dataset")

st.download_button(
    label="Download CSV",
    data=df_amc.to_csv(index=False),
    file_name="amc_music_with_clusters.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption("AMC Music Clustering Dashboard • KMeans • Streamlit")
