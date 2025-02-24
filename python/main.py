#!/usr/bin/env python3

"""Create input files for simulations."""

import argparse
from modules.file_utils import create_base_directory, generate_filename, write_file
from modules.project_loader import detect_project, load_layout, load_settings


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

    project_name = args.project or detect_project()
    settings = load_settings(project_name)
    layout = load_layout(project_name, args.layout)

    config = {
        "ext": settings["file_settings"]["input_file_extension"],
        "base_dir": create_base_directory(layout),
        "base_params": settings["constants"],
    }


if __name__ == "__main__":
    main()
