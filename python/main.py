#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args
from modules.project_loader import (
    detect_project,
    load_layout,
    load_settings,
    load_generator,
)


def main():
    """Main function."""

    args = parse_args()
    project_name = detect_project(args.project)
    generator = load_generator(project_name)
    settings = load_settings(project_name)
    layout = load_layout(args.layout)
    common_generator(generator, settings, layout)


if __name__ == "__main__":
    main()
