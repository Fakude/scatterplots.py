"""Generate a transparent study-time versus marks scatterplot analysis."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_data(seed: int = 12, size: int = 90) -> pd.DataFrame:
    """Create illustrative data, explicitly not records of real learners."""
    rng = np.random.default_rng(seed)
    groups = np.where(np.arange(size) % 2 == 0, "Group A", "Group B")
    hours = np.clip(rng.normal(7, 3, size), 0, 16)
    group_effect = np.where(groups == "Group A", 1.2, -1.2)
    marks = np.clip(47 + hours * 3.2 + group_effect + rng.normal(0, 8, size), 0, 100)
    return pd.DataFrame({"participant_id": [f"P{i:03d}" for i in range(1, size + 1)], "group": groups, "study_hours": hours.round(2), "test_mark": marks.round(2)})


def fit_line(data: pd.DataFrame) -> tuple[float, float, float]:
    x, y = data["study_hours"].to_numpy(), data["test_mark"].to_numpy()
    slope, intercept = np.polyfit(x, y, 1)
    correlation = np.corrcoef(x, y)[0, 1]
    return float(slope), float(intercept), float(correlation)


def create_figure(data: pd.DataFrame, output: str | Path) -> None:
    slope, intercept, correlation = fit_line(data)
    plt.style.use("seaborn-v0_8-whitegrid")
    figure, axis = plt.subplots(figsize=(9, 6), constrained_layout=True)
    colours = {"Group A": "#3b6b8e", "Group B": "#d27a63"}
    for group, subset in data.groupby("group"):
        axis.scatter(subset["study_hours"], subset["test_mark"], label=group, color=colours[group], alpha=.78, edgecolor="white", linewidth=.5)
    x_range = np.linspace(data["study_hours"].min(), data["study_hours"].max(), 100)
    axis.plot(x_range, slope * x_range + intercept, color="#263238", linewidth=2.2, label="Linear trend")
    axis.set(title="Study time and test marks (illustrative data)", xlabel="Weekly study hours", ylabel="Test mark (%)", ylim=(0, 105))
    axis.text(.02, .96, f"Pearson r = {correlation:.2f}\nSlope = {slope:.2f} marks/hour", transform=axis.transAxes, va="top", bbox={"boxstyle": "round,pad=.5", "facecolor": "white", "edgecolor": "#d5d8d8"})
    axis.legend(frameon=False, ncols=3, loc="lower right")
    axis.spines[["top", "right"]].set_visible(False)
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    data = make_data()
    Path("data").mkdir(exist_ok=True)
    data.to_csv("data/study_time.csv", index=False)
    create_figure(data, "outputs/study_time_scatter.png")
    slope, _intercept, correlation = fit_line(data)
    print(f"Generated {len(data)} illustrative records; r={correlation:.3f}, slope={slope:.3f}.")


if __name__ == "__main__":
    main()
