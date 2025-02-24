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


def load_project(project_name):
    """Dynamically imports the correct project settings."""

    try:
        return importlib.import_module(f"settings.{project_name}")
    except ModuleNotFoundError:
        raise ValueError(f"Project settings for '{project_name}' not found.")
