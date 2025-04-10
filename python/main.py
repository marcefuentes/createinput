#!/usr/bin/env python3

"""Create input files for simulations."""

from modules.common_generator import common_generator
from modules.parse_args import parse_args


def main():
    """Main function."""

    args = parse_args()
    print(f"Project: {args.project}, layout: {args.layout}")

    common_generator(args.generator_function, args.settings, args.layout_function)


if __name__ == "__main__":
    main()
