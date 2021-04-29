from pathlib import Path
import os
import re
import shutil

class Generator:
    def __init__(self, config):
        self.config = config
        self.headers = []
        self.footers = []

        self.load_resources()
    
    """
    Generates the entire project.
    """
    def generate(self):
        if not os.path.exists("wgbuild"):
            os.mkdir("wgbuild")

        for f in self.config["files"]:
            # This is the output file's path. It's just the input file, but
            #  inside the wgbuild directory
            outpath = f"wgbuild/{f}"
            os.makedirs(os.path.dirname(outpath), exist_ok=True)

            output = self.genfile(f)
            with open(outpath, mode="w+") as of:
                of.write(output)
        
        for item in self.config["to_copy"]:
            out = f"wgbuild/{item}"

            # We delete the output file/directory if it already exists...
            if os.path.exists(out):
                shutil.rmtree(out)

            # ...and then we recursively copy it over
            shutil.copytree(item, out)

    """
    Loads resources that we will need throughout the program, like
    reading the headers and footers, and storing them inside strings
    """
    def load_resources(self):
        for header in self.config["headers"]:
            self.headers.append(open(header, mode="r").read())

        for footer in self.config["footers"]:
            self.footers.append(open(footer, mode="r").read())

    """
    Generates a file, but doesn't write it. Returns the output file's contents
    """
    def genfile(self, name):
        f = ""

        for header in self.headers:
            f += header

        f += open(name, mode="r").read()

        for footer in self.footers:
            f += footer
        
        for name, fn in self.config["functions"].items():
            # This regex just replaces a function calls with the function output
            f = re.sub(r"\{\{\s?" + name + r"\s?\}\}", fn.invoke(), f)
        
        return f
