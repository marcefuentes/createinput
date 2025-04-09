#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args
from modules.project_loader import get_module_attr


def main():
    """Main function."""

    args = parse_args()
    print(f"Projetc: {args.project}, layout: {args.layout}")
    generator = get_module_attr(f"projects.{args.project}.generator", "generator")
    settings = get_module_attr(f"projects.{args.project}.settings", "settings")
    layout = get_module_attr(f"projects.{args.project}.layouts.{args.layout}", "layout")

    common_generator(generator, settings, layout)


if __name__ == "__main__":
    main()
