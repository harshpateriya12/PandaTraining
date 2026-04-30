def inspect_dataframe(df, name="DataFrame"):
    if df is None:
        print(f"{name} is empty!")
        return

    print(f"\n--- {name} Info ---")
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)
    print("\nFirst 5 Rows:\n", df.head())