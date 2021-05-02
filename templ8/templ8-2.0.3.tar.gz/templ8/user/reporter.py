from dataclasses import dataclass
from pprint import pformat
from typing import Any, List

from art import text2art
from simple_chalk import chalk

from templ8.state.collection import Collection
from templ8.state.initialization import Initialization
from templ8.state.loader import Loader
from templ8.user.flags import Flags
from templ8.utils.strings import indent_lines, truncate_lines


@dataclass
class MessageOptions:
    title: bool = False
    subtitle: bool = False
    block: bool = False
    action: bool = False


@dataclass
class Reporter:
    flags: Flags

    def report(self, msg: str, options: MessageOptions = MessageOptions()) -> None:
        if not self.flags.silent:
            if options.title:
                msg = "\n" + chalk.green(msg)
            elif options.subtitle:
                msg = "\n" + chalk.blue(msg)
            elif options.block:
                msg = "\n" + msg
            elif self.flags.dry_run and options.action:
                msg = indent_lines(msg, "  (Dry run) ")
            else:
                msg = indent_lines(msg, "  ")

            if self.flags.verbosity < 2:
                msg = truncate_lines(msg, 100)

            print(msg)

    def launch(self) -> None:
        self.report(text2art("Templ8", font="ghost"), MessageOptions(block=True))

    def show_object(self, obj: Any, name: str, properties: List[str]) -> None:
        self.report(name, MessageOptions(title=True))
        for prop in properties:
            self.show_property(obj, prop)

    def show_property(self, obj: Any, name: str) -> None:
        self.report(name, MessageOptions(subtitle=True))
        self.report(pformat(getattr(obj, name)))

    def show_loader(self, loader: Loader) -> None:
        self.show_object(
            loader,
            "Loader",
            [
                "collection_sources",
                "collection_names",
                "output_dir",
                "includes",
                "protected",
            ],
        )

        if self.flags.verbosity >= 1:
            self.show_property(loader, "render_context")

            for collection in loader.collections:
                self.show_collection(collection)

        if self.flags.verbosity >= 2:
            self.show_property(loader, "file_paths")

        if self.flags.verbosity >= 3:
            self.show_property(loader, "schema")

    def show_collection(self, collection: Collection) -> None:
        self.show_object(
            collection,
            collection.name,
            [
                "default_variables",
                "default_protected",
                "dynamic_folders",
                "initialization",
            ],
        )

    def clear_top_level(self) -> None:
        self.report("Clearing top level files", MessageOptions(title=True))

    def start_collection(self, collection: Collection) -> None:
        self.report(
            f"Processing collection: {collection.name}",
            MessageOptions(title=True, action=True),
        )

    def protected(self, path: str) -> None:
        self.report(f"Leaving {path} unchanged", MessageOptions(action=True))

    def write_template(self, path: str) -> None:
        self.report(f"Templating {path}", MessageOptions(action=True))

    def write_static(self, path: str) -> None:
        self.report(f"Copying {path}", MessageOptions(action=True))

    def delete(self, path: str) -> None:
        self.report(f"Deleting {path}", MessageOptions(action=True))

    def initialization(self, initialization: Initialization) -> None:
        self.report(
            f"Running {initialization.cmd} in {initialization.cwd}",
            MessageOptions(action=True),
        )
