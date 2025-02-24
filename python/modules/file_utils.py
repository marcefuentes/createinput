from pathlib import Path


def create_base_directory(layout):
    """Create and return the base output directory path."""

    base_parts = [
        "lang" if layout["Language"] else "nolang",
        "shuffle" if layout["Shuffle"] else "noshuffle",
        f"cost{-int(layout['Cost'])}",
        f"{2**layout['GroupSize']}",
    ]
    return Path("_".join(base_parts))


def generate_filename(index, ext):
    """Generate a zero-padded filename."""

    return f"{index:04d}{ext}"


def write_file(file_path, content):
    """Write content to a file."""

    try:
        with file_path.open("w") as f:
            f.writelines(content)
    except IOError as e:
        print(f"Error writing {file_path}: {e}")

