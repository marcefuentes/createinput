"""Settings for the project"""

from projects.cgnr.ces_utils import generate_pairs_ces
from settings.parameters import parameters


def setup():
    """Adapt the parameters to the project"""

    parameters["constants"] = [
        "Seed,1\n",
        "N,12\n",
        "Runs,30\n",
        "Time,21\n",
        "Periods,3\n",
        "MutationSize,-6\n",
        "DeathRate,-7\n",
    ]
    parameters["ces_pairs"] = generate_pairs_ces()
