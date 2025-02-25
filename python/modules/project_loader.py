"""Dynamically loads the correct project settings."""

import os
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

    projects_path = Path(__file__).parent.parent / "projects"
    projects = os.listdir(projects_path)

    if project:
        if project in projects:
            return project
        raise ValueError(f"Project '{project}' not found in {projects_path}")

    current_parts = set(Path.cwd().resolve().parts)
    matching_projects = projects.intersection(current_parts)
    if matching_projects:
        return matching_projects.pop()

    raise ValueError(f"Could not determine the project. Select one of {projects}")


def load_generator(project_name):
    """Dynamically imports the correct generator module."""

    try:
        generator_module = import_module(f"projects.{project_name}.generator")
    except ModuleNotFoundError as exc:
        raise GeneratorDiscoveryError(
            f"Project {project_name} has no generator."
        ) from exc

    generator_function = getattr(generator_module, "generator", None)

    if not generator_function:
        raise GeneratorDiscoveryError(
            f"Project {project_name} has no 'generator' function."
        )

    return generator_function


def load_layout(layout_name):
    """Dynamically imports the correct layout module."""

    return load_module_attr(f"layouts.{layout_name}", "get_layout", LayoutDiscoveryError)

def load_module_attr(module_name, attr_name, error_class):
    try:
        module = import_module(module_name)
    except ModuleNotFoundError:
        raise error_class(f"Module '{module_name}' not found.")

    attr = getattr(module, attr_name, None)
    if not attr:
        raise error_class(f"Module '{module_name}' has no attribute '{attr_name}'.")

    return attr()

def load_settings(project_name):
    """Dynamically imports the correct project settings."""

    return load_module_attr(f"projects.{project_name}.settings", "get_settings", SettingsDiscoveryError)
