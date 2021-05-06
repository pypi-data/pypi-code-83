from enum import Enum

class VisualCompareResult(Enum):
    Match = 0
    ContentMismatch = 1
    FileMismatch = 2
    ProcessingError = 3
    ConversionError = 4
    UnsupportedFileType = 5
    InvalidArguements = 6
    TimeOut = 7
    ReferenceExists = 8
