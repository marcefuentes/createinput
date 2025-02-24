"""Basic."""


def basic(data):
    """Basic."""

    data["mechanisms"] = ["none", "none", "d", "d", "p", "pd"]
    data["givens"] = [0.0, 1.0, 0.0, 1.0, 1.0, 1.0]
    data["pops"] = ["pop_1", "pop_2"]

    return data
