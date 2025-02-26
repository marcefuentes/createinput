"""Basic."""


def get_layout():
    """Returns the layout dictionary."""

    return {
        "Language": [0],
        "Shuffle": [0],
        "Cost": [-3],
        # "Cost,-15, # mgnr
        "GroupSize": [7],
        "mechanisms": ["none", "none", "d", "d", "p", "pd"],
        "Given": [0.0, 1.0, 0.0, 1.0, 1.0, 1.0],
        "Populations": [1, 2],
    }
