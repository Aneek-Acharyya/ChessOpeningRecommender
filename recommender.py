import pandas as pd

df = pd.read_csv("games.csv")

white_df = pd.DataFrame({
    "player": df["white_id"],
    "rating": df["white_rating"],
    "opening": df["opening_name"],
    "result": (df["winner"] == "white").astype(int)
})

black_df = pd.DataFrame({
    "player": df["black_id"],
    "rating": df["black_rating"],
    "opening": df["opening_name"],
    "result": (df["winner"] == "black").astype(int)
})

players_df = pd.concat([white_df, black_df], ignore_index=True)

player_stats = (
    players_df
    .groupby(["player", "opening"])
    .agg(
        games_played=("result", "count"),
        wins=("result", "sum"),
        avg_rating=("rating", "mean")
    )
    .reset_index()
)

player_stats["win_rate"] = (
    player_stats["wins"] /
    player_stats["games_played"] * 100
)

player_stats["experience_score"] = (
    player_stats["games_played"] ** 0.5
)

player_stats["recommendation_score"] = (
    0.7 * player_stats["win_rate"] +
    0.3 * player_stats["experience_score"]
)


def recommend_openings(player):

    player_history = player_stats[
        player_stats["player"] == player
    ]

    if player_history.empty:
        return None

    return player_history.sort_values(
        by=["recommendation_score", "games_played"],
        ascending=False
    ).head(5)


def recommend_by_rating(player):

    history = player_stats[
        player_stats["player"] == player
    ]

    if history.empty:
        return None

    rating = history["avg_rating"].mean()

    similar = players_df[
        (players_df["rating"] >= rating - 100) &
        (players_df["rating"] <= rating + 100)
    ]

    similar = similar[
        similar["player"] != player
    ]

    recommendations = (
        similar.groupby("opening")
        .agg(
            games=("result", "count"),
            wins=("result", "sum")
        )
        .reset_index()
    )

    recommendations["win_rate"] = (
        recommendations["wins"] /
        recommendations["games"] * 100
    )

    recommendations = recommendations[
        recommendations["games"] >= 5
    ]

    return recommendations.sort_values(
        by=["win_rate", "games"],
        ascending=False
    ).head(5)