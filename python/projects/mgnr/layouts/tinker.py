# Tinker

from projects.mgnr.layouts.default import setup as default_setup
from settings.layout import layout


def setup():
    """Setup the layout."""

    default_setup()
    layout["shuffles"] = [0, 1]
    layout["mechanisms"] = ["i", "pi"]
    layout["givens"] = ["1.0", "1.0"]
