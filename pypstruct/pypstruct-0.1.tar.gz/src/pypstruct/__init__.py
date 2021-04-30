from .coordinates import Parser


def parseFilePDB(filename, **kwargs):
    pdbParser = Parser()
    return pdbParser.load(file=filename, **kwargs)