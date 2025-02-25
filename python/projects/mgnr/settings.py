""" Settings for the project """

import numpy as np


def get_settings():
    """Return the settings for the project"""

    return {
        "constants": [
            "Seed,1\n",
            "N,12\n",
            "Runs,30\n",
            "Time,20\n",
            "Periods,3\n",
            "MutationRate,0.01\n",
            "DeathRate,-7\n",
        ],
        "file_settings": {
            "input_file_extension": ".glo",
        },
        "ces_pairs": generate_pairs_ces(),
    }


def generate_pairs_ces():
    """Generate (alpha, logES) pairs."""

    alphas = np.linspace(0.1, 0.9, 11)
    logess = np.linspace(-5.0, 5.0, 11)
    return [(alpha, loges) for alpha in alphas for loges in logess]
