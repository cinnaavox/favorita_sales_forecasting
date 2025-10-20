import pandas as pd
import numpy as np
from typing import Tuple, List
from pathlib import Path

def load_df(path: Path) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {p}")
    if p.suffix.lower() == ".parquet":
        df = pd.read_parquet(p)
    else:
        df = pd.read_csv(p)
    
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

def available_keys(df: pd.DataFrame, store_col="store_nbr", item_col="item_nbr") -> Tuple[List[int], List[int]]:
    stores = sorted(int(s) for s in pd.Series(df[store_col].unique()).dropna().tolist())
    items  = sorted(int(i) for i in pd.Series(df[item_col].unique()).dropna().tolist())
    return stores, items

def filter_window(df: pd.DataFrame, start: str, end: str, time_col="date") -> pd.DataFrame:
    m = (df[time_col] >= pd.to_datetime(start)) & (df[time_col] <= pd.to_datetime(end))
    return df.loc[m].copy()

def filter_series(df: pd.DataFrame, store: int, item: int, store_col="store_nbr", item_col="item_nbr") -> pd.DataFrame:
    m = (df[store_col] == store) & (df[item_col] == item)
    return df.loc[m].copy()

def thin_preview(df: pd.DataFrame, n=5) -> pd.DataFrame:
    if len(df) <= n:
        return df
    head = df.head(n//2)
    tail = df.tail(n - len(head))
    return pd.concat([head, tail])
