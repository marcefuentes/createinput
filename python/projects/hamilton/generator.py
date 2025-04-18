"""Generator fot this project."""

from modules.file_utils import generate_filename, write_file
from settings.parameters import parameters


def generator(mg_params, mg_dir, pop):
    """Main function to generate input files for all parameter combinations."""

    ext = parameters["file_settings"]["input_file_extension"]
    for filename, alpha in enumerate(parameters["alpha_values"]):
        file_path = mg_dir / generate_filename(filename, ext)
        params = mg_params + [
            f"Populations,{pop}\n",
            f"alpha,{alpha}\n",
            "logES,0\n",
            "qBlow,0\n",
            "qBhigh,0\n",
        ]
        write_file(file_path, params)
        print(f"\r{file_path}", end="", flush=True)
    print()
