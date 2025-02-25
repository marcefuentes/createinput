"""Functions to generate input files for the model."""

from modules.file_utils import create_base_directory


def common_generator(generator, settings, layout):
    """Main function to generate input files for all parameter combinations."""

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
                    mg_generator(generator, settings, layout, dirname_params, base_dir)


def mg_generator(generator, settings, layout, dirname_params, base_dir):
    """Generate input files for all parameter combinations."""

    for mechanism, given in zip(layout["mechanisms"], layout["Given"]):
        mg_params = dirname_params + [
            f"PartnerChoice,{1 if 'p' in mechanism else 0}\n",
            f"Reciprocity,{1 if 'd' in mechanism or 'i' in mechanism else 0}\n",
            f"IndirectR,{1 if 'i' in mechanism else 0}\n",
            f"Given,{given}\n",
        ]

        for pop in layout["Populations"]:
            mg_dir = base_dir / mechanism / str(given) / f"pop_{str(pop)}"
            mg_dir.mkdir(parents=True, exist_ok=True)

            generator(mg_params, settings, mg_dir, pop)
