"""Dynamically loads the correct project settings."""

import os
from importlib import import_module


def detect_project():
    """Detects the project based on the execution path."""

    path = os.getcwd()
    for project in ["hamilton", "mgnr", "dgnr"]:  # Add more projects here
        if project in path:
            return project
    return None


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
