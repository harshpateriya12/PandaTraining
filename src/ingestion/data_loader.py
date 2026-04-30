import pandas as pd


class DataLoader:

    def __init__(self, deliveries_path: str, matches_path: str):
        self.deliveries_path = deliveries_path
        self.matches_path = matches_path

    def load_deliveries(self):
        try:
            deliveries_df = pd.read_csv(self.deliveries_path)
            print("Deliveries data loaded successfully")
            return deliveries_df
        except Exception as e:
            print(f"Error loading deliveries data: {e}")
            return None

    def load_matches(self):
        try:
            matches_df = pd.read_csv(self.matches_path)
            print("Matches data loaded successfully")
            return matches_df
        except Exception as e:
            print(f"Error loading matches data: {e}")
            return None