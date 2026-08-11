import json
from datetime import datetime
from pathlib import Path

FILE = "today.json"


def gendate():
    path = Path(FILE)
    if path.exists():
        print("file exists")
        return

    now = datetime.now(tz=None)
    d = {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "microsecond": now.microsecond,
        "total_seconds": now.timestamp(),
    }

    with open(FILE, "w") as f:
        json.dump(d, f)


if __name__ == "__main__":
    gendate()
