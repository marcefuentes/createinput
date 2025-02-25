"""Parses command-line arguments."""

import argparse
import os


def get_available_projects():
    """Return a list of available projects."""

    return [
        d for d in os.listdir("projects") if os.path.isdir(os.path.join("projects", d))
    ]


def get_available_layouts():
    """Return a list of available layouts."""

    return [
        os.path.splitext(d)[0]
        for d in os.listdir("layouts")
        if os.path.isfile(os.path.join("layouts", d))
    ]


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
