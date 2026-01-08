import json
from datetime import datetime
from pathlib import Path
from typing import Any

def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def save_json(path: str, data: dict[str, Any]) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path
