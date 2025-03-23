"""Parses command-line arguments."""

import argparse
from modules.project_loader import (
    detect_project,
    get_available,
)


def parse_args():
    """Parse command-line arguments."""

    available_projects = get_available("projects")
    available_layouts = get_available("layouts")

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, choices=available_projects)
    parser.add_argument(
        "--layout", type=str, default="default", choices=available_layouts
    )

    args = parser.parse_args()
    args.project = detect_project(args.project)

    return args
