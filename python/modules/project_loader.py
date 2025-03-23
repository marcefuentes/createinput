"""Dynamically loads the correct project settings."""

from importlib import import_module
from pathlib import Path


class LayoutDiscoveryError(Exception):
    """Raised when the layout module does not contain the correct function."""


class SettingsDiscoveryError(Exception):
    """Raised when the settings module does not contain the correct function."""


class GeneratorDiscoveryError(Exception):
    """Raised when the generator module does not contain the correct function."""


def detect_project(project=None):
    """Detects all projects in the projects directory."""

    available_projects = set(get_available_projects())

    if project:
        if project in available_projects:
            return project
        raise ValueError(f"Project '{project}' not found")

    current_parts = set(Path.cwd().resolve().parts)
    matching_projects = available_projects.intersection(current_parts)
    if matching_projects:
        return matching_projects.pop()

    raise ValueError(
        f"Could not determine the project. Select one of: {available_projects}"
    )


def find_module_attr(module_name, attr_name, error_class):
    """Dynamically imports a module and returns the specified attribute."""

    try:
        module = import_module(module_name)
    except ModuleNotFoundError as exc:
        raise error_class(f"Module '{module_name}' not found.") from exc

    attr = getattr(module, attr_name, None)
    if not attr:
        raise error_class(f"Module '{module_name}' has no attribute '{attr_name}'.")

    return attr


def get_available_layouts():
    """Return a list of available layouts."""

    layouts_path = Path(__file__).resolve().parent.parent / "layouts"

    return [d.stem for d in layouts_path.iterdir() if d.is_file()]


def get_available_projects():
    """Return a list of available projects."""

    projects_path = Path(__file__).resolve().parent.parent / "projects"

    return [d.name for d in projects_path.iterdir() if d.is_dir()]


def get_generator_function(project):
    """Dynamically imports the correct generator module."""

    try:
        generator_module = import_module(f"projects.{project}.generator")
    except ModuleNotFoundError as exc:
        raise GeneratorDiscoveryError(f"Project {project} has no generator.") from exc

    generator_function = getattr(generator_module, "generator", None)

    if not generator_function:
        raise GeneratorDiscoveryError(f"Project {project} has no 'generator' function.")

    return generator_function


def get_layout(layout_name):
    """Dynamically imports the correct layout module."""

    available_layouts = get_available_layouts()

    if layout_name not in available_layouts:
        raise LayoutDiscoveryError(
            f"Layout '{layout_name}' not found. Select one of: {' '.join(available_layouts)}"
        )

    return find_module_attr(f"layouts.{layout_name}", "layout", LayoutDiscoveryError)


def get_settings(project):
    """Dynamically imports the correct project settings."""

    return find_module_attr(
        f"projects.{project}.settings", "settings", SettingsDiscoveryError
    )
