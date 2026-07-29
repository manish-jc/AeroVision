import pandas as pd


def clean_data(df, save_csv=False):
    """
    Clean the raw aircraft dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw dataframe from OpenSky API

    save_csv : bool
        Save cleaned CSV snapshot (default=False)

    Returns
    -------
    pandas.DataFrame
    """

    print("\n🧹 Cleaning dataset...")

    # -------------------------------
    # Remove duplicate aircraft
    # -------------------------------

    df = df.drop_duplicates(subset="icao24")

    # -------------------------------
    # Clean Callsign
    # -------------------------------

    df["callsign"] = (
        df["callsign"]
        .fillna("Unknown")
        .str.strip()
    )

    # -------------------------------
    # Clean Country
    # -------------------------------

    df["origin_country"] = (
        df["origin_country"]
        .fillna("Unknown")
        .str.strip()
    )

    # -------------------------------
    # Numeric Columns
    # -------------------------------

    numeric_columns = [
        "longitude",
        "latitude",
        "baro_altitude",
        "velocity",
        "true_track",
        "vertical_rate",
        "geo_altitude"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # -------------------------------
    # Remove rows without location
    # -------------------------------

    df = df.dropna(
        subset=["latitude", "longitude"]
    )

    # -------------------------------
    # Fill Missing Values
    # -------------------------------

    df["baro_altitude"] = df["baro_altitude"].fillna(0)
    df["velocity"] = df["velocity"].fillna(0)
    df["true_track"] = df["true_track"].fillna(0)
    df["vertical_rate"] = df["vertical_rate"].fillna(0)

    # -------------------------------
    # Convert Timestamp Columns
    # -------------------------------

    if "time_position" in df.columns:
        df["time_position"] = pd.to_datetime(
            df["time_position"],
            unit="s",
            errors="coerce"
        )

    if "last_contact" in df.columns:
        df["last_contact"] = pd.to_datetime(
            df["last_contact"],
            unit="s",
            errors="coerce"
        )

    # -------------------------------
    # Save CSV (Optional)
    # -------------------------------

    if save_csv:
        df.to_csv(
            "data/processed/aircraft_final.csv",
            index=False
        )
        print("📁 Cleaned CSV snapshot saved.")

    print(f"✅ Cleaning Complete! Rows: {len(df)}")

    return df


# ----------------------------------
# Test
# ----------------------------------

if __name__ == "__main__":

    from fetch_data import fetch_live_data

    df = fetch_live_data()

    df = clean_data(df, save_csv=True)

    print(df.head())