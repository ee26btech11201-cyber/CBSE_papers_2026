"""Simulate the two-dice event and plot its probability distribution."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

trials = 500_000
rng = np.random.default_rng(2026)
rolls = rng.integers(1, 7, size=(trials, 2))
# X=1 when both dice show less than 4; otherwise X=0.
event = np.all(rolls < 4, axis=1).astype(int)
counts = np.bincount(event, minlength=2)
empirical = counts / trials
theoretical = np.array([3 / 4, 1 / 4])

fig, ax = plt.subplots(figsize=(5.8, 4.2))
positions = np.arange(2)
width = 0.36
ax.bar(positions - width / 2, theoretical, width, label="Theoretical", color="steelblue")
ax.bar(positions + width / 2, empirical, width, label="Simulation", color="darkorange")
ax.set_xticks(positions, ["X = 0\nnot both below 4", "X = 1\nboth below 4"])
ax.set_ylabel("Probability")
ax.set_ylim(0, 1)
ax.set_title("Probability distribution for the two-dice event")
ax.grid(axis="y", alpha=0.3)
ax.legend()
fig.tight_layout()

print(f"Trials: {trials:,}")
print(f"P(both numbers < 4), simulated = {empirical[1]:.5f}")
print(f"P(both numbers < 4), exact = {theoretical[1]:.5f} = 1/4")
output = Path(__file__).resolve().parent.parent / "figs" / "4.1.10.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Figure saved to {output}")
