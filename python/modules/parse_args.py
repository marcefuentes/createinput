"""Parses command-line arguments."""

import argparse
from modules.project_loader import (
    detect_project,
    get_available,
    get_module_attr,
)

_args = None


def parse_args():
    """Parse command-line arguments."""

    global _args
    if _args is not None:
        return _args

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
    )

    _args = parser.parse_args()
    _args.project = detect_project(_args.project)

    available_layouts = get_available(f"projects/{_args.project}/layouts", type_="file")
    if _args.layout not in available_layouts:
        parser.error(f"--layout must be one of: {', '.join(available_layouts)}")

    # Load project-specific function and settings
    _args.generator_function = get_module_attr(
        f"projects.{_args.project}.generator", "generator"
    )
    _args.layout_function = get_module_attr(
        f"projects.{_args.project}.layouts.{_args.layout}", "setup"
    )
    _args.parameters_function = get_module_attr(
        f"projects.{_args.project}.settings", "setup"
    )

    return _args
