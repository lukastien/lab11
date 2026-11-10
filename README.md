# lab11 — How Likely Is "Likely"?

Quarto (Python) analysis of the [TidyTuesday](https://github.com/rfordatascience/tidytuesday) dataset **"How likely is 'likely'?"** (2026-03-10), based on Adam Kucharski's online quiz where participants assigned numeric probabilities (0–100%) to 19 probability phrases and completed pairwise comparisons.

## Research questions

1. Which phrases do people most disagree on when translating them into numeric probabilities?
2. Which demographic backgrounds tend to assign higher probabilities (operationally: more "optimistic") after controlling for phrase?

## Findings

1. **Phrase disagreement.** People disagree most on mid-range, hedged phrases: *Realistic Possibility* (SD = 20.6), *Could Happen* (18.2), *Might Happen* (17.7), and *May Happen* (17.0). Extreme phrases such as *About Even*, *Almost Certain*, and *Almost No Chance* show much tighter agreement.
2. **Demographic “optimism”.** Defining optimism as higher phrase-adjusted probability ratings, education and country show the largest group spreads (~2.7 percentage points). High school respondents rate highest and postgraduates lowest; among countries with n ≥ 30, the United States is highest and Norway lowest. English-background differences are negligible. All demographic spreads are far smaller than phrase-level disagreement.

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
