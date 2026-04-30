from src.ingestion.data_loader import DataLoader
from src.utils.inspector import inspect_dataframe


def main():
    # File paths
    deliveries_path = "data/deliveries.csv"
    matches_path = "data/matches.csv"

    # Initialize loader
    loader = DataLoader(deliveries_path, matches_path)

    # Load data
    deliveries_df = loader.load_deliveries()
    matches_df = loader.load_matches()

    # Inspect data
    inspect_dataframe(deliveries_df, "Deliveries DataFrame")
    inspect_dataframe(matches_df, "Matches DataFrame")


if __name__ == "__main__":
    main()