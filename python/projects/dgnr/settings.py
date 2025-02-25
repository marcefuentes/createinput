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
        "q_b_pairs": generate_pairs_q_b(),
    }


def generate_pairs_ces():
    """Generate (alpha, logES) pairs."""

    alphas = np.linspace(0.1, 0.9, 3)
    logess = np.linspace(-5.0, 5.0, 3)
    return [(alpha, loges) for alpha in alphas for loges in logess]


def generate_pairs_q_b():
    """Generate (qBlow, qBhigh) pairs."""

    num = 20
    pairs = []
    for k in range(num):
        q_blow = k / num
        num_new = num - k
        q_bhighs = np.linspace(q_blow + 1 / num, 1.0, num_new)
        q_bhighs = np.round(q_bhighs, decimals=6)
        pairs.extend([(q_blow, q_bhigh) for q_bhigh in q_bhighs])
    return pairs
