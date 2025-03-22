"""Parses command-line arguments."""

import argparse
from modules.project_loader import get_available_projects, get_available_layouts


def parse_args():
    """Parse command-line arguments."""

    available_projects = get_available_projects()
    available_layouts = get_available_layouts()

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, choices=available_projects)
    parser.add_argument(
        "--layout", type=str, default="default", choices=available_layouts
    )

    return parser.parse_args()
