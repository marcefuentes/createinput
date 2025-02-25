"""Functions to generate input files for the model."""

from modules.file_utils import generate_filename, write_file


def generator(m_g_params, settings, mg_dir, pop):
    """Main function to generate input files for all parameter combinations."""

    ext = settings["file_settings"]["input_file_extension"]
    for filename, b in enumerate(settings["b_values"]):
        file_path = mg_dir / generate_filename(filename, ext)
        params = m_g_params + [
            f"Populations,{pop}\n",
            f"b,{b}\n",
        ]
        write_file(file_path, params)
        print(f"\r{file_path}", end="", flush=True)
    print()
