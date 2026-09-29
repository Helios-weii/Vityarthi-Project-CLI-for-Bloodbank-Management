import pickle
from pathlib import Path

fold = Path(__file__).resolve().parent.parent / "data"
fold.mkdir(exist_ok=True)

def load(fn):
    p = fold / fn
    if not p.exists():
        return []
    try:
        with p.open("rb") as f:
            x = pickle.load(f)
            return x if isinstance(x, list) else []
    except (EOFError, pickle.PickleError, OSError):
        return []

def save(fn, rec):
    p = fold / fn
    with p.open("wb") as f:
        pickle.dump(rec, f)
