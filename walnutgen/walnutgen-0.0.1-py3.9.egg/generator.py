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
    
    def generate(self):
        for f in self.config["files"]:
            outpath = f"wgbuild/{Path(f).relative_to('./')}"
            os.makedirs(os.path.dirname(outpath), exist_ok=True)

            output = self.genfile(f)
            with open(outpath, mode="w+") as of:
                of.write(output)
        
        for item in self.config["to_copy"]:
            shutil.copytree(item, f"wgbuild/{item}")

    def load_resources(self):
        for header in self.config["headers"]:
            self.headers.append(open(header, mode="r").read())

        for footer in self.config["footers"]:
            self.footers.append(open(footer, mode="r").read())

    def genfile(self, name):
        f = ""

        for header in self.headers:
            f += header

        f += open(name, mode="r").read()

        for footer in self.footers:
            f += footer
        
        for name, fn in self.config["functions"].items():
            f = re.sub(r"\{\{\s?" + name + r"\s?\}\}", fn.invoke(), f)
        
        return f
