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


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project", type=str, help="Project name (e.g., hamilton, mgnr)"
    )
    parser.add_argument(
        "--layout", type=str, required=True, help="Layout name (e.g., basic, unit)"
    )
    return parser.parse_args()


def main(args):
    """Main function."""

    project_name = detect_project(args.project)
    generator = load_generator(project_name)
    settings = load_settings(project_name)
    layout = load_layout(args.layout)
    common_generator(generator, settings, layout)


if __name__ == "__main__":
    args = parse_args()
    main(args)
