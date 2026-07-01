from pathlib import Path
import csv

def load_csv(path: str | Path) -> list[dict]:
    """Lire un fichier CSV et retourner une liste de dictionnaires."""
    records = []

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append({
                "id": int(row["id"]),
                "name": row["name"],
                "age": int(row["age"]),
                "score": float(row["score"])
            })

    return records


def filter_by_min_score(records: list[dict], min_score: float) -> list[dict]:
    """Retourner les étudiants dont le score est supérieur ou égal à min_score."""
    return [record for record in records if record["score"] >= min_score]


def average_score(records: list[dict]) -> float:
    """Calculer la moyenne des scores."""
    if not records:
        return 0.0

    total = sum(record["score"] for record in records)
    return total / len(records)


def summarize(records: list[dict]) -> dict:
    """Retourner un résumé statistique des scores."""
    if not records:
        return {
            "count": 0,
            "avg_score": 0.0,
            "max_score": 0.0,
            "min_score": 0.0
        }

    scores = [record["score"] for record in records]

    return {
        "count": len(records),
        "avg_score": average_score(records),
        "max_score": max(scores),
        "min_score": min(scores)
    }