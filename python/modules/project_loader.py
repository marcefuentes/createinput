"""Dynamically loads project dictionaries and functions."""

from importlib import import_module
from pathlib import Path


class DiscoveryError(Exception):
    """Raised when a module or attribute cannot be found."""


def detect_project(project=None):
    """Detects all projects in the projects directory."""

    available_projects = set(get_available_projects())

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


def get_available_projects():
    """Return a list of available projects."""
    projects_path = Path(__file__).resolve().parent.parent / "projects"
    return [d.name for d in projects_path.iterdir() if d.is_dir()]


def get_available_layouts():
    """Return a list of available layouts."""
    layouts_path = Path(__file__).resolve().parent.parent / "layouts"
    return [d.stem for d in layouts_path.iterdir() if d.is_file()]


def get_module_attribute(module_path, attr_name, expected_type=None):
    """Dynamically imports a module and retrieves the specified attribute.

    Args:
        module_path (str): Module path to import.
        attr_name (str): Attribute name to retrieve.
        expected_type (type, optional): Expected type of the attribute.

    Returns:
        The requested attribute if found and valid.

    Raises:
        DiscoveryError: If the module or attribute is missing or has the wrong type.
    """
    try:
        module = import_module(module_path)
    except ModuleNotFoundError as exc:
        raise DiscoveryError(f"Module '{module_path}' not found.") from exc

    attr = getattr(module, attr_name, None)

    if expected_type and not isinstance(attr, expected_type):
        raise DiscoveryError(
            f"'{attr_name}' in '{module_path}' is not of type {expected_type.__name__}."
        )

    return attr
