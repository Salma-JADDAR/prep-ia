from src.dataset import CsvDataset


if __name__ == "__main__":
    ds = CsvDataset("Étudiants")

    ds.load_from_csv("data/sample.csv")

    print("Dataset:", ds)
    print("Total records:", ds.row_count)

    passed = ds.filter_by_column("score", 10)

    print("Admis (score >= 10):", len(passed))

    print("Columns:", ds.columns)

    print("Résumé:", ds.summary())