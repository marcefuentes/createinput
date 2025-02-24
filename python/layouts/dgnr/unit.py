"""Unit."""


def unit(data):
    """Basic."""

    mechanism = ""

    if data["p"]:
        mechanism += "p"

    if data["d"]:
        mechanism += "d"

    if data["i"]:
        mechanism += "i"

    if mechanism == "":
        mechanism = "none"

    data["mechanisms"] = [mechanism]
    data["givens"] = [data["given"]]

    return data
