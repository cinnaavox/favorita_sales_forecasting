from pathlib import Path

ART_DIR = Path("artifacts_local")

MODEL_PATH = ART_DIR / "xgb_booster.json"
FEATURES_PATH = ART_DIR / "features.json"
CONFORMAL_PATH = ART_DIR / "conformal_intervals.json"

DATE_MIN = "2014-01-01"
DATE_MAX = "2014-03-31"

TIME_COL = "date"
STORE_COL = "store_nbr"
ITEM_COL = "item_nbr"

MAX_SHOW_ROWS = 2000
