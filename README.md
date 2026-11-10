# lab11 — How Likely Is "Likely"?

Quarto (Python) analysis of the [TidyTuesday](https://github.com/rfordatascience/tidytuesday) dataset **"How likely is 'likely'?"** (2026-03-10), based on Adam Kucharski's online quiz where participants assigned numeric probabilities (0–100%) to 19 probability phrases and completed pairwise comparisons.

## Research questions

1. Which phrases do people most disagree on when translating them into numeric probabilities?
2. Which demographic backgrounds tend to assign higher probabilities (operationally: more "optimistic") after controlling for phrase?

## Dataset source

Raw CSVs are downloaded from:

`https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-03-10/`

Files:

- `absolute_judgements.csv`
- `pairwise_comparisons.csv`
- `respondent_metadata.csv`

## Folder structure

```
lab11/
├── analysis/          # Quarto report (.qmd) and rendered HTML
├── data/
│   ├── raw/           # Downloaded TidyTuesday CSVs
│   └── processed/     # Derived tables from the analysis
├── figures/           # Exported PNG figures
├── scripts/           # Data download script
└── README.md
```

## Reproduce

From the project root (`lab11/`):

```bash
python scripts/01_download.py
quarto render analysis/how_likely_is_likely.qmd
```

Requires Python 3 with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scipy`, plus Quarto with a Jupyter `python3` kernel.
