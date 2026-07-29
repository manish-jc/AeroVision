import pandas as pd


def add_features(df, save_csv=False):
    """
    Add engineered features to the cleaned aircraft dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned aircraft dataframe

    save_csv : bool
        Save engineered CSV snapshot (default=False)

    Returns
    -------
    pandas.DataFrame
    """

    print("\n⚙️ Performing Feature Engineering...")

    # -----------------------------------
    # Speed (m/s → km/h)
    # -----------------------------------

    df["speed_kmh"] = (df["velocity"] * 3.6).round(2)

    # -----------------------------------
    # Altitude (m → ft)
    # -----------------------------------

    df["altitude_ft"] = (
        df["baro_altitude"] * 3.28084
    ).round(2)

    # -----------------------------------
    # Direction
    # -----------------------------------

    def get_direction(angle):

        if pd.isna(angle):
            return "Unknown"

        directions = [
            "North",
            "North-East",
            "East",
            "South-East",
            "South",
            "South-West",
            "West",
            "North-West"
        ]

        index = int(((angle + 22.5) % 360) / 45)

        return directions[index]

    df["direction"] = df["true_track"].apply(get_direction)

    # -----------------------------------
    # Flight Phase
    # -----------------------------------

    def get_flight_phase(row):

        if row["on_ground"]:
            return "On Ground"

        if row["vertical_rate"] > 2:
            return "Climbing"

        if row["vertical_rate"] < -2:
            return "Descending"

        return "Cruising"

    df["flight_phase"] = df.apply(
        get_flight_phase,
        axis=1
    )

    # -----------------------------------
    # Speed Category
    # -----------------------------------

    def speed_category(speed):

        if speed < 250:
            return "Slow"

        elif speed < 700:
            return "Medium"

        return "Fast"

    df["speed_category"] = df["speed_kmh"].apply(
        speed_category
    )

    # -----------------------------------
    # Last Seen (seconds)
    # -----------------------------------

    current_time = pd.Timestamp.utcnow().tz_localize(None)

    df["last_seen_seconds"] = (
        current_time - df["last_contact"]
    ).dt.total_seconds()

    # -----------------------------------
    # Optional CSV Snapshot
    # -----------------------------------

    if save_csv:

        df.to_csv(
            "data/processed/aircraft_featured.csv",
            index=False
        )

        print("📁 Engineered CSV snapshot saved.")

    print("✅ Feature Engineering Complete!")

    print(f"Total Columns : {len(df.columns)}")

    print(f"Total Aircraft : {len(df)}")

    return df


# ----------------------------------
# Test
# ----------------------------------

if __name__ == "__main__":

    from fetch_data import fetch_live_data
    from clean_data import clean_data

    df = fetch_live_data()

    df = clean_data(df)

    df = add_features(
        df,
        save_csv=True
    )

    print(df.head())