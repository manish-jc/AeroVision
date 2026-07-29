import json
import requests
import pandas as pd
from scripts.auth import get_access_token


def fetch_live_data(save_json=True, save_csv=False):
    """
    Fetch live aircraft data from OpenSky API.

    Parameters
    ----------
    save_json : bool
        Save raw API response as JSON (default=True)

    save_csv : bool
        Save fetched dataframe as CSV (default=False)

    Returns
    -------
    pandas.DataFrame
    """

    # ----------------------------------
    # Authentication
    # ----------------------------------

    token = get_access_token()

    if token is None:
        raise Exception("Authentication failed!")

    # ----------------------------------
    # API Request
    # ----------------------------------

    url = "https://opensky-network.org/api/states/all"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"API Error {response.status_code}\n{response.text}"
        )

    data = response.json()

    print("✅ Live data fetched successfully!")

    # ----------------------------------
    # Save Raw JSON (Optional)
    # ----------------------------------

    if save_json:

        with open("data/raw/aircraft_raw.json", "w") as file:
            json.dump(data, file, indent=4)

        print("📁 Raw JSON saved.")

    # ----------------------------------
    # Create DataFrame
    # ----------------------------------

    columns = [
        "icao24",
        "callsign",
        "origin_country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "true_track",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source"
    ]

    df = pd.DataFrame(data["states"], columns=columns)

    print(f"✈ Aircraft Found : {len(df)}")

    # ----------------------------------
    # Save CSV (Optional)
    # ----------------------------------

    if save_csv:

        df.to_csv(
            "data/processed/aircraft_clean.csv",
            index=False
        )

        print("📁 CSV Snapshot Saved.")

    return df


# ----------------------------------
# Test
# ----------------------------------

if __name__ == "__main__":

    df = fetch_live_data()

    print(df.head())