#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args


def main():
    """Main function."""

    print(f"Project: {parse_args().project}, layout: {parse_args().layout}")

    parse_args().parameters_function()
    parse_args().layout_function()

    common_generator()


if __name__ == "__main__":
    main()
