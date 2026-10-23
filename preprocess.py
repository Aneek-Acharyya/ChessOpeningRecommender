import pandas as pd


def load_dataset(path="games.csv"):
    return pd.read_csv(path)


def create_players_dataframe(df):

    white_df = pd.DataFrame({
        "player": df["white_id"],
        "rating": df["white_rating"],
        "opening": df["opening_name"],
        "eco": df["opening_eco"],
        "result": (df["winner"] == "white").astype(int)
    })

    black_df = pd.DataFrame({
        "player": df["black_id"],
        "rating": df["black_rating"],
        "opening": df["opening_name"],
        "eco": df["opening_eco"],
        "result": (df["winner"] == "black").astype(int)
    })

    players_df = pd.concat([white_df, black_df], ignore_index=True)

    return players_df


def create_player_statistics(players_df):

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
        player_stats["games_played"]
    ) * 100

    player_stats["experience_score"] = (
        player_stats["games_played"] ** 0.5
    )

    player_stats["recommendation_score"] = (
        0.7 * player_stats["win_rate"] +
        0.3 * player_stats["experience_score"]
    )

    return player_stats