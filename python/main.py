#!/usr/bin/env python3

"""Create input files for simulations."""

import argparse
from modules.file_utils import create_base_directory, generate_filename, write_file
from modules.project_loader import detect_project, load_layout, load_project


def main():
    """Main function."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project", type=str, help="Project name (e.g., hamilton, mgnr)"
    )
    parser.add_argument(
        "--layout", type=str, required=True, help="Layout name (e.g., basic, unit)"
    )
    args = parser.parse_args()

    # Auto-detect project if not provided
    project_name = args.project or detect_project()
    if not project_name:
        raise ValueError("Could not determine project. Please use --project.")

    # Load the correct project settings and layout
    project_settings = load_project(project_name)
    layout_module = load_layout(project_name, args.layout)

    print(f"Running for project: {project_name}, layout: {args.layout}")
    print(f"Using settings: {project_settings.settings}")
    print(f"Using layout: {layout_module}")


if __name__ == "__main__":
    main()
