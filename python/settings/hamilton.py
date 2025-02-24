""" Settings for the project """

import numpy as np

def settings():
    """ Return the settings for the project """

    return {
    "constants": {
        "N": 12,
        "Runs": 30,
        "Time": 20,
        "Periods": 3,
        "MutationRate": 0.01,
        "DeathRate": -7,
    },
    "b_parameters": {
        "b_min": -7,
        "b_max": 3,
        "num": 11,
    },
    "file_settings": {
        "input_file_extension": ".glo",
    },
}

def generate_values(config):
    """ Generate b values."""

    return np.linspace(
        config["b_parameters"]["b_min"],
        config["b_parameters"]["b_max"],
        config["b_parameters"]["num"],
    )
