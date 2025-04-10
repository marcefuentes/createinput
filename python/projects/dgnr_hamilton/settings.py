"""Settings for the project"""

import numpy as np
from settings.settings import settings


def generate_arrays():
    """Generate arrays for the project."""

    alpha_values = np.linspace(-7, 3, 11)


def change_settings():
    """Adapt the settings to the project"""

    settings["constants"] = [
        "Seed,1\n",
        "N,12\n",
        "Runs,30\n",
        "Time,20\n",
        "Periods,3\n",
        "MutationRate,0.01\n",
        "DeathRate,-7\n",
        "Ces,0\n",
    ]
    settings["file_settings"] = {
        "input_file_extension": ".glo",
    }
    settings["alpha_values"] = generate_arrays()
