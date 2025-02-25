#!/usr/bin/env python3

"""Create input files for simulations."""

import argparse
from modules.common_generator import common_generator
from modules.project_loader import (
    detect_project,
    load_layout,
    load_settings,
    load_generator,
)


def main():
    """Main function."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project", type=str, help="Project name (e.g., hamilton, mgnr)"
    )
    parser.add_argument(
        "--layout", type=str, required=True, help="Layout name (e.g., basic, unit)"
    )
    args = parser.parse_args()

    project_name = detect_project(args.project)
    generator = load_generator(project_name)
    settings = load_settings(project_name)
    layout = load_layout(project_name, args.layout)
    common_generator(generator, settings, layout)


if __name__ == "__main__":
    main()
