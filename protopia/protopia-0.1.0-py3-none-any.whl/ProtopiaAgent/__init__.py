import os
import sys
import inspect

curr_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
currentdir = os.path.dirname(curr_path)
sys.path.insert(0, currentdir)

from ProtopiaAgent.agent import Agent
