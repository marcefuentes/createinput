"""Generate pairs for the project."""

import numpy as np


def generate_arrays():
    """Generate arrays for the project."""

    alphas = np.linspace(0.1, 0.9, 21)
    logess = np.linspace(-5.0, 5.0, 21)
    return alphas, logess


def generate_pairs_ces():
    """Generate (alpha, logES) pairs."""

    alphas, logess = generate_arrays()
    return [(alpha, loges) for alpha in alphas for loges in logess]
