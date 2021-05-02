class MissingOutputDir(Exception):
    def __init__(self) -> None:
        super().__init__("Missing output directory from input configuration")
