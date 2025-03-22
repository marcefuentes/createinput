#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args
from modules.project_loader import (
    detect_project,
    get_layout,
    get_settings,
    get_generator_function,
)


def main():
    """Main function."""

    args = parse_args()
    project_name = detect_project(args.project)
    generator = get_generator_function(project_name)
    settings = get_settings(project_name)
    layout = get_layout(args.layout)

    common_generator(generator, settings, layout)


if __name__ == "__main__":
    main()
