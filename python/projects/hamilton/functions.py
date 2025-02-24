"""Functions to generate input files for the model."""

from modules.file_utils import generate_filename, create_base_directory, write_file
from modules.generate_utils import build_base_parameters


def generator(settings, layout):
    """Main function to generate input files for all parameter combinations."""

    ext = settings["file_settings"]["input_file_extension"]
    settings_params = settings["constants"]
    config = {}

    for lang in layout["Language"]:
        config["Language"] = lang
        for shuffle in layout["Shuffle"]:
            config["Shuffle"] = shuffle
            for cost in layout["Cost"]:
                config["Cost"] = cost
                for group_size in layout["GroupSize"]:
                    config["GroupSize"] = group_size
                    base_dir = create_base_directory(config)
                    dirname_params = settings_params + [
                        f"Language,{lang}\n",
                        f"Shuffle,{shuffle}\n",
                        f"Cost,{cost}\n",
                        f"GroupSize,{group_size}\n",
                    ]
                    for mechanism, given in zip(layout["mechanisms"], layout["Given"]):
                        m_g_params = dirname_params + [
                            f"PartnerChoice,{1 if 'p' in mechanism else 0}\n",
                            f"Reciprocity,{1 if 'd' in mechanism or 'i' in mechanism else 0}\n",
                            f"IndirectR,{1 if 'i' in mechanism else 0}\n",
                            f"Given,{given}\n",
                        ]

                        for pop in layout["Populations"]:
                            mg_dir = (
                                base_dir / mechanism / str(given) / f"pop_{str(pop)}"
                            )
                            mg_dir.mkdir(parents=True, exist_ok=True)

                            for filename, b in enumerate(settings["b_values"]):
                                file_path = mg_dir / generate_filename(filename, ext)
                                params = m_g_params + [
                                    f"Populations,{pop}\n",
                                    f"b,{b}\n",
                                ]
                                write_file(file_path, params)
                                print(f"\r{file_path}", end="", flush=True)
                            print()
