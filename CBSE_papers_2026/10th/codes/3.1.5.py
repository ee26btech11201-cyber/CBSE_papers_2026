"""Simulate many two-dice rolls and plot the sum distribution."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

trials = 500_000
rng = np.random.default_rng(2026)
dice = rng.integers(1, 7, size=(trials, 2))
sums = dice.sum(axis=1)
values = np.arange(2, 13)
observed = np.array([(sums == value).mean() for value in values])
ways = np.array([1,2,3,4,5,6,5,4,3,2,1])
theoretical = ways / 36
event_empirical = np.isin(sums, [6,12]).mean()

fig, ax = plt.subplots(figsize=(6.0, 4.1))
ax.bar(values-.19, theoretical, width=.38, color="steelblue", label="Exact probability")
ax.bar(values+.19, observed, width=.38, color="darkorange", label="Simulation")
ax.set(xticks=values, xlabel="Sum of the two dice", ylabel="Probability",
       title=f"Two dice: {trials:,} simulated rolls")
ax.grid(axis="y",alpha=.25); ax.legend(); fig.tight_layout()
print(f"P(sum divisible by 6), simulated = {event_empirical:.5f}")
print("Exact probability = 6/36 = 1/6")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.5.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
