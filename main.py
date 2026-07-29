from scripts.fetch_data import fetch_live_data
from scripts.clean_data import clean_data
from scripts.feature_engineering import add_features


def run_pipeline(save_json=True, save_csv=False, verbose=True):
    """
    Run the complete AeroVision ETL pipeline.

    Parameters
    ----------
    save_json : bool
        Save raw API response as JSON.

    save_csv : bool
        Save processed CSV snapshot.

    verbose : bool
        Display progress messages.

    Returns
    -------
    pandas.DataFrame
        Final engineered dataframe.
    """

    if verbose:
        print("=" * 60)
        print("✈️  AeroVision - Live Flight ETL Pipeline")
        print("=" * 60)

    # ----------------------------------
    # Step 1 - Fetch Live Data
    # ----------------------------------
    df = fetch_live_data(
        save_json=save_json,
        save_csv=False
    )

    # ----------------------------------
    # Step 2 - Clean Data
    # ----------------------------------
    df = clean_data(
        df,
        save_csv=False
    )

    # ----------------------------------
    # Step 3 - Feature Engineering
    # ----------------------------------
    df = add_features(
        df,
        save_csv=save_csv
    )

    if verbose:
        print("\n✅ Pipeline Completed Successfully!")
        print(f"\n📊 Total Aircraft : {len(df)}")
        print(f"📈 Total Columns  : {len(df.columns)}")

    return df


if __name__ == "__main__":

    df = run_pipeline(
        save_json=True,
        save_csv=True,
        verbose=True
    )

    print("\nFirst Five Records:\n")
    print(df.head())