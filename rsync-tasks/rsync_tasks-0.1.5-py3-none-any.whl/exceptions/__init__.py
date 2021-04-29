class RsyncTasksError(Exception):
    pass


class RsyncNotAvailable(RsyncTasksError):
    def __str__(self) -> str:
        return "'rsync' tool not found"


class ConfigError(RsyncTasksError):
    pass


class ConfigNotFound(ConfigError):
    def __init__(self, file: str):
        self._file = file

    def __str__(self) -> str:
        return "Configuration file '{}' not found".format(self._file)


class InvalidConfig(ConfigError):
    pass


class TaskError(RsyncTasksError):
    pass


class SourcePathNotExist(TaskError):
    def __init__(self, path: str):
        self._path = path

    def __str__(self) -> str:
        return "Source path '{}' does not exist".format(self._path)


class LocalPathNotWritable(TaskError):
    def __init__(self, path: str):
        self._path = path

    def __str__(self) -> str:
        return "Directory '{}' is not writable".format(self._path)


class IdentityFileUnreadable(TaskError):
    def __init__(self, file: str):
        self._file = file

    def __str__(self) -> str:
        return "Identity file '{}' is not readable".format(self._file)


class TargetFailed(TaskError):
    def __init__(self, path: str):
        self._path = path

    def __str__(self) -> str:
        return "Failed sync of '{}'".format(self._path)


class TaskFailed(TaskError):
    pass
