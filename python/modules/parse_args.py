"""Parses command-line arguments."""

import argparse
import os
from pathlib import Path


def get_available_projects():
    """Return a list of available projects."""

    projects_path = Path(__file__).parent.parent / "projects"
    
    return [d.name for d in projects_path.iterdir() if d.is_dir()]


def get_available_layouts():
    """Return a list of available layouts."""

    layouts_path = Path(__file__).parent.parent / "layouts"

    return [d.stem for d in layouts_path.iterdir() if d.is_file()]


def parse_args():
    """Parse command-line arguments."""

    available_projects = get_available_projects()
    available_layouts = get_available_layouts()
    project_help = f"Options: {', '.join(available_projects)}"
    layout_help = f"Options: {', '.join(available_layouts)}"

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, help=project_help)
    parser.add_argument("--layout", type=str, required=True, help=layout_help)

    return parser.parse_args()
