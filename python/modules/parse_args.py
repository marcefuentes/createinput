"""Parses command-line arguments."""

import argparse
from pathlib import Path
from modules.project_loader import get_available_projects, get_available_layouts


def parse_args():
    """Parse command-line arguments."""

    available_projects = get_available_projects()
    available_layouts = get_available_layouts()
    project_help = f"Options: {', '.join(available_projects)}"
    layout_help = f"Options: {', '.join(available_layouts)}"

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, help=project_help)
    parser.add_argument("--layout", type=str, default="default", help=layout_help)

    return parser.parse_args()
