# scripts/01_download.py
from pathlib import Path
import urllib.request

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-01-13/africa.csv"
Path("data/raw").mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(url, "data/raw/africa.csv")