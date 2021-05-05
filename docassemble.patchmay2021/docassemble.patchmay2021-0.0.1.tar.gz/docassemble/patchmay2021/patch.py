# pre-load
import pathlib
import importlib
import re
import sys
import shutil

try:
  this_file = str(pathlib.Path(__file__).parent.absolute())
  dest_file = re.sub(r'/site-packages/docassemble/.*', '/site-packages/docassemble/base/functions.py', this_file)
  source_file = re.sub(r'/site-packages/docassemble/.*', '/site-packages/docassemble/patchmay2021/data/sources/functions', this_file)

  current_version = str(importlib.import_module('docassemble.base').__version__)

  if current_version == '1.1.101':
    sys.stderr.write("docassemble.patchmay2021: patched functions.py by copying " + source_file + " to " + dest_file + "\n")
    shutil.copyfile(source_file, dest_file)
  else:
    sys.stderr.write("docassemble.patchmay2021: did not patch because version was " + current_version + " \n")
except:
  sys.stderr.write("docassemble.patchmay2021: did not patch because there was an error\n")
