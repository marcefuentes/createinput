"""Basic."""

def get_layout():
    """Returns the layout dictionary."""

    return {
        "dir_variables": {
            "Language": 0,
            "Shuffle": 0,
            "Cost": -3,
            "GroupSize": 7,
        },
        "mechanisms": ["none", "none", "d", "d", "p", "pd"],
        "givens": [0.0, 1.0, 0.0, 1.0, 1.0, 1.0],
    }
