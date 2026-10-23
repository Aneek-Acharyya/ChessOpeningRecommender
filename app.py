import streamlit as st
import plotly.express as px
from recommender import recommend_openings, recommend_by_rating

st.set_page_config(
    page_title="AI Chess Opening Recommender",
    page_icon="♟",
    layout="wide"
)

st.title("♟ AI-Based Chess Opening Recommendation System")

st.markdown("""
### Improve Your Chess Opening Strategy

This application analyzes historical chess games and recommends the most effective chess openings based on:

- 🎯 Previous game performance
- 📈 Win percentage
- ♟ Number of games played
- ⭐ Recommendation score
- 👥 Similar-rated players

Enter a chess username to receive personalized opening recommendations.
""")

st.divider()

player = st.text_input(
    "Enter Chess Username",
    placeholder="Example: taranga"
)

if st.button("🔍 Recommend Openings", use_container_width=True):

    personal = recommend_openings(player)

    if personal is None:

        st.error("Player not found or not enough games.")

    else:

        personal = personal.round(2)

        if "player" in personal.columns:
            personal = personal.drop(columns=["player"])

        best = personal.iloc[0]

        st.success(
            f"🏆 Best Recommended Opening: **{best['opening']}**"
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "♟ Games Played",
            int(best["games_played"])
        )

        col2.metric(
            "✅ Win Rate",
            f"{best['win_rate']:.2f}%"
        )

        col3.metric(
            "⭐ Recommendation Score",
            f"{best['recommendation_score']:.2f}"
        )

        col4.metric(
            "📈 Average Rating",
            int(best["avg_rating"])
        )

        st.info(
            "Recommendations are calculated using win percentage, number of games played, and recommendation score."
        )

        st.divider()

        st.subheader("🏆 Personalized Opening Recommendations")

        st.dataframe(
            personal,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("📈 Win Rate of Your Best Openings")

        fig = px.bar(
            personal,
            x="opening",
            y="win_rate",
            text="win_rate",
            color="win_rate",
            title="Win Rate of Your Best Openings"
        )

        fig.update_layout(
            xaxis_title="Chess Opening",
            yaxis_title="Win Rate (%)",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        rating = recommend_by_rating(player)

        if rating is not None:

            rating = rating.round(2)

            st.divider()

            st.subheader("⭐ Recommended Openings From Similar-Rated Players")

            st.dataframe(
                rating,
                use_container_width=True,
                hide_index=True
            )

            st.subheader("📊 Win Rates of Similar-Rated Players")

            fig2 = px.bar(
                rating,
                x="opening",
                y="win_rate",
                text="win_rate",
                color="win_rate",
                title="Recommended Openings From Similar-Rated Players"
            )

            fig2.update_layout(
                xaxis_title="Chess Opening",
                yaxis_title="Win Rate (%)",
                height=500
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            csv = rating.to_csv(index=False)

            st.download_button(
                "📥 Download Recommendations",
                csv,
                "recommendations.csv",
                "text/csv"
            )

st.divider()

st.markdown("""
## About This Project

This AI-Based Chess Opening Recommendation System recommends chess openings using:

- Historical Chess Games Dataset
- Player Win Percentage
- Number of Games Played
- Recommendation Score
- Similar Rating-Based Recommendation

### Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

### Recommendation Technique

- Historical Performance Analysis
- Score-Based Ranking
- Similar Rating Filtering

This project demonstrates a recommendation system for suggesting effective chess openings based on a player's historical performance and players with similar ratings.
""")

with st.expander("📖 How Recommendations Are Generated"):

    st.markdown("""
### Recommendation Process

1. Historical chess games are analyzed.

2. Every player's win rate is calculated.

3. Recommendation Score is computed as:

**Recommendation Score = 0.7 × Win Rate + 0.3 × Experience Score**

4. Openings are ranked according to this score.

5. Openings played by similar-rated players are also recommended.
""")

st.divider()

st.caption(
    "Developed by Aneek Acharyya | Manipal University Jaipur | Department of Artificial Intelligence & Machine Learning"
)