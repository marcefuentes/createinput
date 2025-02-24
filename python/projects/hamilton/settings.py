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
        "b_values": np.linspace(-7, 3, num=11),
    }
