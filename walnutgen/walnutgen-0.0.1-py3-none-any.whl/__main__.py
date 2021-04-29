import sys
import os

from walnutgen.generator import Generator

sys.path.append(os.getcwd())
import wgconfig  # From the CWD

def main():    
    generator = Generator(wgconfig.config)
    generator.generate()

if __name__ == "__main__":
    main()
