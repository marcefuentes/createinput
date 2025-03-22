#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args
from modules.project_loader import (
    get_generator_function,
    get_layout,
    get_settings,
)


def main():
    """Main function."""

    args = parse_args()
    generator = get_generator_function(args.project)
    settings = get_settings(args.project)
    layout = get_layout(args.layout)

    common_generator(generator, settings, layout)


if __name__ == "__main__":
    main()
