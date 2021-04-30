import os
import shutil
from dataclasses import dataclass
from pathlib import Path

from templ8.state.collection import Collection
from templ8.state.loader import Loader
from templ8.user.flags import Flags
from templ8.user.reporter import Reporter
from templ8.utils.paths import full_listdir, path_tail


@dataclass
class Generator:
    flags: Flags
    loader: Loader
    reporter: Reporter

    def sequence(self) -> None:
        if self.loader.inputs.clear_top_level:
            self.reporter.clear_top_level()
            self.clear_top_level()

        for collection in self.loader.collections:
            self.reporter.start_collection(collection)
            self.write_static(collection)
            self.write_templates(collection)
            self.initialization(collection)

    def is_protected(self, target: str) -> bool:
        return os.path.exists(target) and os.path.normpath(target) in [
            os.path.normpath(os.path.join(self.loader.output_dir, path))
            for path in self.loader.protected
        ]

    def clear_top_level(self) -> None:
        Path(self.loader.output_dir).mkdir(parents=True, exist_ok=True)
        for top_level_path in full_listdir(self.loader.output_dir):
            if os.path.isfile(top_level_path):
                if self.is_protected(top_level_path):
                    self.reporter.protected(top_level_path)
                else:
                    self.reporter.delete(top_level_path)

                    if not self.flags.dry_run:
                        os.remove(top_level_path)

    def write_static(self, collection: Collection) -> None:
        for static in collection.static_files:
            output_path = static.output_path(
                self.loader.output_dir,
                collection.dynamic_folders,
                self.loader.render_context,
            )

            if self.is_protected(output_path):
                self.reporter.protected(output_path)
            else:
                self.reporter.write_static(output_path)

                if not self.flags.dry_run:
                    Path(path_tail(output_path)).mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(static.source_path, output_path)

    def write_templates(self, collection: Collection) -> None:
        for template in collection.templates:
            output_path = template.output_path(
                self.loader.output_dir,
                collection.dynamic_folders,
                self.loader.render_context,
            )

            if self.is_protected(output_path):
                self.reporter.protected(output_path)
            else:
                self.reporter.write_template(output_path)

                if not self.flags.dry_run:
                    Path(path_tail(output_path)).mkdir(parents=True, exist_ok=True)
                    with open(output_path, "w") as stream:
                        stream.write(
                            template.parse(
                                self.loader.render_context,
                                self.loader.loader_paths,
                            )
                        )

    def initialization(self, collection: Collection) -> None:
        for initialization in collection.initialization:
            self.reporter.initialization(initialization)

            if not self.flags.dry_run:
                initialization.run(
                    self.loader.output_dir,
                    collection.dynamic_folders,
                    self.loader.render_context,
                )
