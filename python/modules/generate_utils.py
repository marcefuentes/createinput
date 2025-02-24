"""Utility functions for generating parameter files."""


def build_base_parameters(constants, variables):
    """Construct base parameter lines common to all files."""

    constant_lines = [f"{key},{value}\n" for key, value in constants.items()]
    variable_lines = [f"{key},{value}\n" for key, value in variables.items()]

    return constant_lines + variable_lines
