"""Parses command-line arguments."""

import argparse
from modules.project_loader import (
    detect_project,
    get_available,
    get_module_attr,
)


def parse_args():
    """Parse command-line arguments."""

    if hasattr(parse_args, "args_cache"):
        return parse_args.args_cache

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

    args = parser.parse_args()
    args.project = detect_project(args.project)

    available_layouts = get_available(f"projects/{args.project}/layouts", type_="file")
    if args.layout not in available_layouts:
        parser.error(f"--layout must be one of: {', '.join(available_layouts)}")

    # Load project-specific function and settings
    args.generator_function = get_module_attr(
        f"projects.{args.project}.generator", "generator"
    )
    args.layout_function = get_module_attr(
        f"projects.{args.project}.layouts.{args.layout}", "setup"
    )
    args.parameters_function = get_module_attr(
        f"projects.{args.project}.settings", "setup"
    )

    parse_args.cache_args = args
    return args
