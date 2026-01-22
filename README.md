🎧 Amazon Music Clustering & Recommendation System
📌 Project Overview

The Amazon Music Clustering & Recommendation System is an unsupervised machine learning project that groups songs based on their audio characteristics and provides song recommendations using cluster similarity.

Instead of relying on user history, this system leverages content-based features such as rhythm, mood, and energy to identify similar songs. The final solution is deployed as an interactive Streamlit dashboard.

🎯 Problem Statement

With a large number of songs available on music platforms, discovering similar music becomes challenging.
This project aims to:

Automatically cluster songs based on audio features

Understand musical patterns within each cluster

Recommend similar songs using clustering results

Provide an interactive visualization dashboard

📊 Dataset Description

The dataset contains ~95,000 songs with detailed audio and metadata attributes.

Key Audio Features Used

Danceability – How suitable a track is for dancing

Energy – Intensity and activity level

Tempo – Speed of the track (BPM)

Valence – Musical positivity (happy vs sad)

Acousticness – Presence of acoustic elements

Loudness – Overall sound intensity

Speechiness – Presence of spoken words

Instrumentalness – Instrumental dominance

Liveness – Audience presence detection

Other Metadata

Song name

Artist name

Popularity score

Duration (converted from milliseconds to minutes)

Release date

🧠 Methodology
1️⃣ Data Preprocessing

Removed duplicates and verified missing values

Converted duration from milliseconds → minutes

Dropped non-relevant identifiers (song ID, artist ID, names)

Selected only numerical audio features

2️⃣ Feature Scaling

Used StandardScaler to normalize all audio features so that:

Each feature contributes equally to clustering

Distance-based algorithms perform correctly

3️⃣ Dimensionality Reduction (PCA)

Applied Principal Component Analysis (PCA)

Reduced data to 2 components for visualization

Retained maximum variance while simplifying analysis

📌 PCA helped in:

Visualizing clusters

Reducing computational complexity

4️⃣ Clustering Techniques
🔹 KMeans Clustering

Used Elbow Method to identify optimal clusters

Evaluated using Silhouette Score

Final model trained with 4 clusters

🔹 DBSCAN (Exploratory)

Used to detect potential outliers

Compared density-based clustering behavior

5️⃣ Cluster Evaluation

Silhouette Score used to measure cluster separation

Cluster-wise feature averages calculated

Heatmaps and bar charts used for interpretation

🎼 Cluster Profiling & Interpretation

Each cluster represents a distinct musical style:

Cluster	Description
Cluster 0	Calm / Mixed Mood
Cluster 1	Workout / Feel-Good
Cluster 2	Speech-Heavy / Experimental
Cluster 3	Chill Acoustic

Clusters were labeled using average audio feature values such as energy, acousticness, and valence.

🎶 Recommendation System

A content-based recommendation approach is implemented:

How it Works

User selects a song

System identifies the song’s cluster

Recommends top popular songs from the same cluster

✔ No user history required
✔ Fast and interpretable

📊 Streamlit Dashboard Features

The project includes an interactive Streamlit web app with:

🎵 Song selection & recommendations

📌 Cluster-wise song exploration

🔥 Top tracks per cluster

📊 Feature statistics and summaries

🎶 Tempo distribution visualization

⬇ Download clustered dataset as CSV

🛠 Tech Stack

Programming Language: Python

Data Handling: Pandas, NumPy

Machine Learning: Scikit-learn

Visualization: Matplotlib, Seaborn

Deployment: Streamlit

📁 Project Structure
Amazon-Music-Clustering-Recommendation/
│
├── data/
│   └── single_genre_artists.csv
│
├── notebooks/
│   └── amazon_music_clustering.ipynb
│
├── app.py
├── reports/
│   └── amazon_music_clustering.pdf
│
├── outputs/
│   ├── AMC_Music_Clustered_Final.csv
│   └── AMC_Cluster_Profiles.csv
│
└── README.md

📈 Results & Insights

Songs naturally group based on mood and intensity

High-energy tracks form workout clusters

Acoustic and low-energy songs form chill clusters

Clustering improves recommendation relevance

🔮 Future Enhancements

🎧 Integration with real-time music APIs

🧠 Deep learning–based song embeddings

👤 User-based & hybrid recommendation systems

🎼 Genre-aware clustering

📱 Deployment on cloud platforms

✅ Conclusion

This project demonstrates how unsupervised machine learning can be effectively used to analyze music patterns and build a content-based recommendation system. The Streamlit dashboard makes the model interpretable, interactive, and user-friendly.
