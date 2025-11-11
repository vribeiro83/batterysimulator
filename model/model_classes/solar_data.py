import logging
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
import csv

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

@dataclass
class SolarRecord:
    datetime: datetime
    produced_wh: float
    consumed_wh: int
    exported_wh: float
    imported_wh: int

class SolarData:
    def __init__(self, filepath: str):
        self.records: list[SolarRecord] = []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Local time, format: "08/01/2025 00:00"
                ts = datetime.strptime(row["Date/Time"], "%m/%d/%Y %H:%M")

                produced_wh = int(row["Energy Produced (Wh)"])
                exported_wh = int(row["Exported to Grid (Wh)"])
                consumed_wh = int(row["Energy Consumed (Wh)"])
                imported_wh = int(row["Imported from Grid (Wh)"])

                self.records.append(
                    SolarRecord(
                        datetime=ts,
                        produced_wh=produced_wh,
                        consumed_wh=consumed_wh,
                        exported_wh=exported_wh,
                        imported_wh=imported_wh,
                    )
                )
