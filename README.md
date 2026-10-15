# Study Time Scatterplot Analysis

This project transforms a basic scatterplot exercise into a reproducible association analysis. It generates a documented **synthetic** example dataset, compares two illustrative groups, fits a linear trend, and reports Pearson correlation and slope directly on the chart.

## Important data note

The 90 records are simulated for demonstration. The chart shows association, not causation, and makes no claim about real students or groups.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python analyse_study_time.py
```

This creates `data/study_time.csv` and `outputs/study_time_scatter.png`.

## Test

```bash
python -m unittest discover -s tests -v
```

## Continuous integration

[![Python CI](https://github.com/Fakude/scatterplots.py/actions/workflows/ci.yml/badge.svg)](https://github.com/Fakude/scatterplots.py/actions/workflows/ci.yml)

GitHub Actions installs requirements and runs the deterministic unit tests on Python 3.12 for every push and pull request. The workflow is in `.github/workflows/ci.yml`.
