"""Settings for the project"""

import numpy as np


settings = {
    "constants": [
        "Seed,1\n",
        "N,12\n",
        "Runs,30\n",
        "Time,20\n",
        "Periods,3\n",
        "MutationRate,0.01\n",
        "DeathRate,-7\n",
        "Ces,0\n",
    ],
    "file_settings": {
        "input_file_extension": ".glo",
    },
    "alpha_values": np.linspace(-7, 3, num=11),
}
