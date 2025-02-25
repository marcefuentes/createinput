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

    current_path = Path.cwd().resolve()

    for proj in projects:
        if proj in current_path.parts:
            return proj

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


def load_layout(project_name, layout_name):
    """Dynamically imports the correct layout module."""

    try:
        layout_module = import_module(f"projects.{project_name}.layouts.{layout_name}")
    except ModuleNotFoundError as exc:
        raise LayoutDiscoveryError(
            f"Project {project_name} has no layout '{layout_name}'."
        ) from exc

    layout_function = getattr(layout_module, "get_layout", None)

    if not layout_function:
        raise LayoutDiscoveryError(
            f"Layout '{layout_name}' of '{project_name}' has no 'get_layout' function."
        )

    return layout_function()


def load_settings(project_name):
    """Dynamically imports the correct project settings."""

    try:
        settings_module = import_module(f"projects.{project_name}.settings")
    except ModuleNotFoundError as exc:
        raise SettingsDiscoveryError(
            f"Project '{project_name}' has no settings."
        ) from exc

    settings_function = getattr(settings_module, "get_settings", None)

    if not settings_function:
        raise SettingsDiscoveryError(
            f"Project '{project_name}' has no 'get_settings' function."
        )

    return settings_function()
