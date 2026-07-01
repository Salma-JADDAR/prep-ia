from src.utils import load_csv, filter_by_min_score, average_score, summarize

if __name__ == "__main__":
    records = load_csv("data/sample.csv")

    print("Total records:", len(records))

    passed = filter_by_min_score(records, min_score=10)
    print("Admis (score >= 10):", len(passed))

    print("Average score:", average_score(records))

    print("Résumé:", summarize(records))