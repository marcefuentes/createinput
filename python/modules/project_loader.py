"""Dynamically loads project dictionaries and functions."""

from importlib import import_module
from pathlib import Path


def detect_project(project=None):
    """Detects all projects in the projects directory."""

    available_projects = set(get_available("projects"))

    if project:
        if project in available_projects:
            return project
        raise ValueError(f"Project '{project}' not found.")

    current_parts = set(Path.cwd().resolve().parts)
    matching_projects = available_projects.intersection(current_parts)
    if matching_projects:
        return matching_projects.pop()

    raise ValueError(
        f"Could not determine the project. Select one of: {available_projects}"
    )


def get_available(options):
    """Return a list of available projects."""

    projects_path = Path(__file__).resolve().parent.parent / options
    return [d.name for d in projects_path.iterdir() if d.is_dir()]


def get_module_attribute(module_path, attr_name):
    """Dynamically imports a module and retrieves the specified attribute.

    Args:
        module_path (str): Module path to import.
        attr_name (str): Attribute name to retrieve.

    Returns:
        The requested attribute if found.
    """

    module = import_module(module_path)
    attr = getattr(module, attr_name, None)

    return attr
