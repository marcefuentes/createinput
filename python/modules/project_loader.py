"""Dynamically loads the correct project settings."""

import os
from importlib import import_module
from pathlib import Path

class ProjectDiscoveryError(Exception): pass

def discover_projects():
    """Discovers all projects in the 'layouts' directory."""

    layouts_dir = Path(__file__).parent / "layouts"
    settings_dir = Path(__file__).parent / "settings"

    try:
        layouts = set(os.listdir(layouts_dir))
    except FileNotFoundError:
        layouts = set()
        print("No 'layouts' directory found.")

    try:
        settings = set(os.listdir(settings_dir))
    except FileNotFoundError:
        settings = set()
        print("No 'settings' directory found.")

    if not layouts or not settings:
        raise ProjectDiscoveryError("No projects found. 'layouts' or 'settings' empty.")

    projects = layouts.intersection(settings)

    return projects


def detect_project():
    """Detects the project based on the execution path."""

    projects = discover_projects()

    path = os.getcwd()
    for project in projects:
        if project in path:
            return project

    return list(projects)[0]


def load_layout(project_name, layout_name):
    """Dynamically imports the correct layout module."""

    try:
        layout_module = import_module(f"layouts.{project_name}.{layout_name}")
    except ModuleNotFoundError:
        raise ValueError(
            f"Project {project_name} has no layout '{layout_name}'."
        )
    layout_function = getattr(layout_module, "return_layout", None)
    if not layout_function:
        raise ValueError(
            f"Layout '{layout_name}' of '{project_name}' has no 'return_layout' function."
        )
    return layout_function()


def load_settings(project_name):
    """Dynamically imports the correct project settings."""

    try:
        settings_module = import_module(f"settings.{project_name}")
    except ModuleNotFoundError:
        raise ValueError(f"Project '{project_name}' has no settings.")
    settings_function = getattr(settings_module, "return_settings", None)
    if not settings_function:
        raise ValueError(f"Project '{project_name}' has no 'return settings' function.")
    return settings_function()
