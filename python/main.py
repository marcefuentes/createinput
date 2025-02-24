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
    settings_module = load_project(project_name)
    settings = settings_module.settings()

    layout_module = load_layout(project_name, args.layout)
    layout_function = getattr(layout_module, args.layout, None)
    if not layout_function:
        raise ValueError(f"Could not find layout {args.layout} in {project_name}.")
    layout = layout_function()

    config = {
        "ext": settings["file_settings"]["input_file_extension"],
        "base_dir": create_base_directory(layout),
        "base_params": settings["constants"],
    }

    print(settings, layout)

if __name__ == "__main__":
    main()
