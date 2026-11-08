# code by A.Chaitanya
"""Simulate two-dice rolls with NumPy's RNG and plot their sum PMF."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

trials = 500_000
rng = np.random.default_rng(seed=2026)
dice = rng.integers(1, 7, size=(trials, 2))
sums = dice.sum(axis=1)
values = np.arange(2, 13)
observed = np.array([(sums == value).mean() for value in values])
ways = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
theoretical = ways / 36

fig, ax = plt.subplots(figsize=(6.0, 4.1))
width = 0.38
ax.bar(values - width / 2, theoretical, width=width,
       color="steelblue", label="Exact PMF")
ax.bar(values + width / 2, observed, width=width,
       color="darkorange", label="Simulated PMF")
ax.set(xticks=values, xlabel="Sum of the two dice", ylabel="Probability",
       title=f"Two dice: {trials:,} simulated rolls")
ax.grid(axis="y", alpha=0.25)
ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / "figs" / "1.2.4.png"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches="tight")
