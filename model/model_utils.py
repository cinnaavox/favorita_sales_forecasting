import json
import numpy as np
import pandas as pd
import xgboost as xgb
from pathlib import Path
from typing import Dict, Tuple, Optional

def load_artifacts(model_path: Path, features_path: Path, conformal_path: Optional[Path]=None):
    booster = xgb.Booster()
    booster.load_model(str(model_path))

    with open(features_path, "r") as f:
        feats_cfg = json.load(f)
    features = feats_cfg.get("features") or feats_cfg.get("FEATURES")
    target   = feats_cfg.get("target")   or feats_cfg.get("TARGET")

    conformal = None
    if conformal_path and conformal_path.exists():
        with open(conformal_path, "r") as f:
            conformal = json.load(f)

    return booster, features, target, conformal

def ensure_features(df: pd.DataFrame, features: list) -> pd.DataFrame:

    X = df.copy()
    X = X.replace([np.inf, -np.inf], np.nan)
    missing = [c for c in features if c not in X.columns]
    if missing:
        raise ValueError(f"Fehlende Feature-Spalten: {missing}")
    X = X[features].apply(pd.to_numeric, errors="coerce")
    
    meds = X.median(numeric_only=True)
    X = X.fillna(meds)
    return X

def predict_xgb(booster: xgb.Booster, X_df: pd.DataFrame) -> np.ndarray:
    d = xgb.DMatrix(X_df.values)
    return booster.predict(d)

def apply_conformal(pred: np.ndarray, conformal: Optional[Dict]) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
    if not conformal:
        return None, None
    qL = conformal.get("qL90") or conformal.get("qL") or conformal.get("qL_90")
    qH = conformal.get("qH90") or conformal.get("qH") or conformal.get("qH_90")
    if qL is None or qH is None:
        return None, None
    return pred + float(qL), pred + float(qH)
