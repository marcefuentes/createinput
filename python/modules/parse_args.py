"""Parses command-line arguments."""

import argparse
from modules.project_loader import (
    detect_project,
    get_available,
)


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        type=str,
        choices=get_available("projects", type_="dir"),
    )
    parser.add_argument(
        "--layout",
        type=str,
        default="default",
        choices=get_available("layouts", type_="file"),
    )

    args = parser.parse_args()
    args.project = detect_project(args.project)

    return args
