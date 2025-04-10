"""Settings for the project"""

from projects.dgnr_hamilton.utils import generate_arrays
from settings.parameters import parameters


def setup():
    """Adapt the parameters to the project"""

    parameters["constants"] = [
        "Seed,1\n",
        "N,12\n",
        "Runs,30\n",
        "Time,20\n",
        "Periods,3\n",
        "MutationRate,0.01\n",
        "DeathRate,-7\n",
        "Ces,0\n",
    ]
    parameters["alpha_values"] = generate_arrays()
