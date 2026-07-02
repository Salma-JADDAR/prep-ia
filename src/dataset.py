from src.utils import load_csv
class Dataset:
    def __init__(self, name: str):
        self.name = name
        self._records: list[dict] = []

    def load(self, records: list[dict]) -> None:
        """Charge les enregistrements en mémoire."""
        self._records = records

    @property
    def row_count(self) -> int:
        return len(self._records)

    @property
    def columns(self) -> list[str]:
        """Retourne les noms des colonnes."""
        if not self._records:
            return []

        return list(self._records[0].keys())

    def summary(self) -> dict:
        """Retourne un résumé du dataset."""
        return {
            "name": self.name,
            "row_count": self.row_count,
            "columns": self.columns
        }

    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, rows={self.row_count})"
    
class CsvDataset(Dataset):
    def __init__(self, name: str):
        super().__init__(name)

    def load_from_csv(self, path: str) -> None:
        """Charge les données depuis un fichier CSV."""
        records = load_csv(path)
        self.load(records)

    def filter_by_column(self, column: str, min_value: float) -> list[dict]:
        """Filtre les enregistrements."""
        return [
            record
            for record in self._records
            if record[column] >= min_value
        ]    
    
class FilteredDataset(CsvDataset):
    def top_n(self, column: str, n: int) -> list[dict]:
        return sorted(
            self._records,
            key=lambda x: x[column],
            reverse=True
        )[:n]