from dataclasses import dataclass


@dataclass
class Flags:
    verbosity: int
    dry_run: bool
    silent: bool
