""" Settings for the project """

project = {
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
    "ces": {
        "alpha_min": 0.1,
        "alpha_max": 0.9,
        "loges_min": -5.0,
        "loges_max": 5.0,
        "num": 3,
    },

    "input_file_extension": ".glo",
    "q_b_num": 20,
}
