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
        "file_settings": {
            "input_file_extension": ".glo",
        },
        "b_values": np.linspace(-7, 3, num=11),
}
