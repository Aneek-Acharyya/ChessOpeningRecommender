# ♟ AI-Based Chess Opening Recommendation System

## 📖 Project Overview

The AI-Based Chess Opening Recommendation System is a recommendation application that suggests the best chess openings for a player based on their historical game performance and the performance of players with similar ratings.

The system analyzes previous chess games, computes a recommendation score using win rate and playing experience, and recommends openings that maximize a player's chances of success.

---

## 🎯 Objectives

- Recommend the best chess openings for a player.
- Analyze a player's historical performance.
- Compare players with similar ratings.
- Visualize recommendation results using interactive charts.
- Provide an easy-to-use web interface.

---

## ✨ Features

- Personalized opening recommendations
- Similar-rated player recommendations
- Recommendation score calculation
- Win rate analysis
- Interactive data visualization using Plotly
- Download recommendations as CSV
- User-friendly Streamlit interface

---

## 📂 Dataset

Dataset: **games.csv**

The dataset contains over **20,000 chess games** and includes information such as:

- White Player
- Black Player
- Player Ratings
- Winner
- Opening Name
- Opening ECO Code

---

## 🧠 Recommendation Methodology

The recommendation system follows these steps:

1. Load and preprocess the chess dataset.
2. Calculate player statistics.
3. Compute:
   - Number of games played
   - Number of wins
   - Win percentage
4. Calculate the Recommendation Score using:

Recommendation Score = 0.7 × Win Rate + 0.3 × Experience Score

5. Rank openings based on the recommendation score.
6. Recommend additional openings played by players with similar ratings.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly

---

## 📁 Project Structure

```
ChessOpeningRecommender/
│
├── app.py
├── recommender.py
├── preprocess.py
├── games.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Install the required libraries:

```
pip install -r requirements.txt
```

2. Run the application:

```
streamlit run app.py
```

3. Open the browser and enter a chess username.

---

## 📊 Output

The application provides:

- Best Recommended Opening
- Win Rate
- Recommendation Score
- Personalized Opening Recommendations
- Similar-Rated Player Recommendations
- Interactive Charts
- CSV Download Option

---

## 🚀 Future Improvements

- User login system
- Opening style classification (Aggressive, Defensive, Positional)
- Machine Learning-based recommendation model
- Player rating prediction
- Live integration with Chess.com or Lichess APIs

---

## 👨‍💻 Developer

**Aneek Acharyya**

Department of Artificial Intelligence & Machine Learning

Manipal University Jaipur

---

## 📜 License

This project was developed for academic purposes.