"""Dynamically loads project dictionaries and functions."""

from importlib import import_module
from pathlib import Path


def detect_project(project=None):
    """Detects all projects in the projects directory."""

    available_projects = set(get_available_projects())

    if project:
        if project in available_projects:
            return project
        raise ValueError(f"Project '{project}' not found in {available_projects}.")

    current_parts = set(Path.cwd().resolve().parts)
    matching_projects = available_projects.intersection(current_parts)
    if matching_projects:
        return matching_projects.pop()

    raise ValueError(
        f"Could not determine the project. Select one of: {available_projects}"
    )


def get_available_layouts(project):
    """Returns available layouts, preferring project over base_gnr."""

    def layout_files(path):
        return {f.stem for f in path.glob("*.py") if f.is_file()}

    base_path = Path(__file__).resolve().parent.parent / "projects"
    project_path = base_path / project / "layouts"
    base_path = base_path / "base_gnr" / "layouts"

    project_layouts = layout_files(project_path) if project_path.exists() else set()
    base_layouts = layout_files(base_path) if base_path.exists() else set()

    return sorted(project_layouts.union(base_layouts - project_layouts))


def get_available_projects():
    """Return a list of available projects."""

    projects_path = Path(__file__).resolve().parent.parent / "projects"

    return sorted(d.name for d in projects_path.iterdir() if d.is_dir())


def get_module_attr(project, module_path, attr_name):
    """Dynamically imports a module and retrieves the specified attribute."""

    for project_source in [project, "base_gnr"]:
        try:
            module = import_module(f"projects.{project_source}.{module_path}")
            attr = getattr(module, attr_name, None)
            if attr is not None:
                return attr
        except (ModuleNotFoundError, AttributeError):
            continue
    raise ImportError(
        f"Module '{module_path}' not found in project '{project}' or 'base_gnr'."
    )
