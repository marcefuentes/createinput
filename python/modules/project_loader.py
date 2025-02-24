"""Dynamically loads the correct project settings."""

import os
import importlib


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
        module = importlib.import_module(f"layouts.{project_name}.{layout_name}")
    except ModuleNotFoundError:
        raise ValueError(
            f"Project {project_name} has no layout '{layout_name}'."
        )
    function = getattr(module, layout_name, None)
    if not function:
        raise ValueError(
            f"Layout '{layout_name}' in project '{project_name}' has no function."
        )
    return function()


def load_settings(project_name):
    """Dynamically imports the correct project settings."""

    try:
        module = importlib.import_module(f"settings.{project_name}")
    except ModuleNotFoundError:
        raise ValueError(f"Project '{project_name}' has no settings.")
    function = getattr(module, "settings", None)
    if not function:
        raise ValueError(f"Project '{project_name}' has no settings function.")
    return function()
