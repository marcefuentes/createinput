""" Settings for the project """

settings = {
    "constants": {
        "N": 12,
        "Runs": 30,
        "Time": 20,
        "Periods": 3,
        "MutationRate": 0.01,
        "DeathRate": -7,
    },
    "variables": {
        "Language": 0,
        "Shuffle": 0,
        "Cost": -3,
        "GroupSize": 7,
    },
    "b_layout": {
        "b_min": -7,
        "b_max": 3,
        "num": 11,
    },
    "input_file_extension": ".glo",
}

def generate_values():
    """ Generate b values."""

    return np.linspace(settings["b_layout"]["b_min"], settings["b_layout"]["b_max"], settings["b_layout"]["num"])
