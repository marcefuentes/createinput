"""Settings for the project"""

import numpy as np
from settings.settings import settings


def generate_arrays():
    """Generate arrays for the project."""

    alphas = np.linspace(0.1, 0.9, 21)
    logess = np.linspace(-5.0, 5.0, 21)
    return alphas, logess


def generate_pairs_ces():
    """Generate (alpha, logES) pairs."""

    alphas, logess = generate_arrays()
    return [(alpha, loges) for alpha in alphas for loges in logess]


def change_settings():
    """Adapt the settings to the project"""

    settings["constants"] = (
        [
            "Seed,1\n",
            "N,12\n",
            "Runs,30\n",
            "Time,21\n",
            "Periods,3\n",
            "qBMutationSize,-6\n",
            "GrainMutationSize,-6\n",
            "DeathRate,-7\n",
        ],
    )
    settings["file_settings"] = {
        "input_file_extension": ".glo",
    }
    settings["ces_pairs"] = generate_pairs_ces()
