"""Download TidyTuesday 'How likely is likely?' CSVs into data/raw/."""

from pathlib import Path
from urllib.request import urlretrieve

BASE_URL = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
    "main/data/2026/2026-03-10"
)
FILES = [
    "absolute_judgements.csv",
    "pairwise_comparisons.csv",
    "respondent_metadata.csv",
]


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    for filename in FILES:
        dest = raw_dir / filename
        if dest.exists():
            print(f"Skipping {filename}: already exists at {dest}")
            continue
        url = f"{BASE_URL}/{filename}"
        print(f"Downloading {filename} from {url}...")
        urlretrieve(url, dest)
        print(f"Saved {filename} to {dest}")


if __name__ == "__main__":
    main()
