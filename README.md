## 🎧 Amazon Music Clustering & Recommendation System

## 📌 Overview
The **Amazon Music Clustering & Recommendation System** is an **unsupervised machine learning** project that groups songs based on their audio characteristics and recommends similar tracks using **cluster similarity**.

Unlike traditional recommendation systems that rely on user listening history, this project follows a **content-based approach**, leveraging intrinsic audio features such as mood, rhythm, and energy.  
The final solution is deployed as an **interactive Streamlit dashboard** for easy exploration and recommendations.

---

## 🎯 Problem Statement
With millions of songs available on music streaming platforms, discovering similar and relevant music is increasingly difficult.

This project aims to:
- Automatically cluster songs based on audio features
- Identify hidden musical patterns
- Recommend similar songs without user history
- Provide an interactive visualization dashboard

---

## 📊 Dataset Description
- **Total Songs:** ~95,000
- **Source:** Amazon Music Dataset
- **Type:** Audio features + metadata

### 🎵 Audio Features Used
- **Danceability** – Suitability of a track for dancing  
- **Energy** – Intensity and activity level  
- **Tempo** – Speed of the track (BPM)  
- **Valence** – Musical positivity (happy vs sad)  
- **Acousticness** – Presence of acoustic elements  
- **Loudness** – Overall sound intensity  
- **Speechiness** – Presence of spoken words  
- **Instrumentalness** – Instrumental dominance  
- **Liveness** – Audience presence detection  

### 📌 Additional Metadata
- Song name  
- Artist name  
- Popularity score  
- Duration (converted from milliseconds to minutes)  
- Release date  

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing
- Removed duplicate records
- Verified and handled missing values
- Converted song duration from milliseconds → minutes
- Dropped non-relevant identifiers (IDs, names)
- Selected only numerical audio features

---

### 2️⃣ Feature Scaling
- Applied **StandardScaler**
- Ensured equal contribution from all features
- Improved performance of distance-based algorithms

---

### 3️⃣ Dimensionality Reduction (PCA)
- Applied **Principal Component Analysis (PCA)**
- Reduced features to **2 principal components** for visualization
- Retained maximum variance

**Benefits of PCA:**
- Improved cluster visualization
- Reduced computational complexity

---

### 4️⃣ Clustering Techniques

#### 🔹 KMeans Clustering
- Used **Elbow Method** to determine optimal clusters
- Evaluated using **Silhouette Score**
- Final model trained with **4 clusters**

#### 🔹 DBSCAN (Exploratory)
- Used to identify outliers
- Compared density-based clustering behavior

---

### 5️⃣ Cluster Evaluation
- Used **Silhouette Score** to measure cluster separation
- Calculated cluster-wise average feature values
- Visualized results using heatmaps and bar charts

---

## 🎼 Cluster Profiling & Interpretation

| Cluster | Description |
|-------|------------|
| Cluster 0 | Calm / Mixed Mood |
| Cluster 1 | Workout / Feel-Good |
| Cluster 2 | Speech-Heavy / Experimental |
| Cluster 3 | Chill Acoustic |

Clusters were labeled based on dominant audio characteristics such as **energy, acousticness, and valence**.

---

## 🎶 Recommendation System

### 🔍 Approach: Content-Based Recommendation
- User selects a song
- System identifies the song’s cluster
- Recommends **top popular songs from the same cluster**

**Advantages:**
- ✔ No user history required  
- ✔ Fast and interpretable  
- ✔ Scalable for large datasets  

---

## 📊 Streamlit Dashboard Features
- 🎵 Song selection & recommendations  
- 📌 Cluster-wise song exploration  
- 🔥 Top tracks per cluster  
- 📊 Audio feature statistics and summaries  
- 🎶 Tempo distribution visualization  
- ⬇ Download clustered dataset as CSV  

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Visualization:** Matplotlib, Seaborn  
- **Web Application:** Streamlit  

---

## 📁 Project Structure

```
Amazon-Music-Clustering-Recommendation/
│
├── data/
│   └── single_genre_artists.csv
│
├── notebooks/
│   └── amazon_music_clustering.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── reports/
│   └── amazon_music_clustering.pdf
│
├── outputs/
│   ├── AMC_Music_Clustered_Final.csv
│   └── AMC_Cluster_Profiles.csv
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📈 Results & Insights
- Songs naturally group based on **mood and intensity**
- High-energy tracks form workout-focused clusters
- Acoustic and low-energy tracks form chill clusters
- Clustering improves recommendation relevance

---

## 🔮 Future Enhancements
- 🎧 Integration with real-time music APIs  
- 🧠 Deep learning–based song embeddings  
- 👤 User-based and hybrid recommendation systems  
- 🎼 Genre-aware clustering  
- ☁ Cloud deployment  

---

## ✅ Conclusion
This project demonstrates how **unsupervised machine learning** can be used to uncover musical patterns and build a **content-based music recommendation system**.  
The **Streamlit dashboard** makes the system interactive, interpretable, and practical for real-world use.

---
