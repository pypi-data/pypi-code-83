import sys
import os

from generator import Generator

sys.path.append(os.getcwd())
import wgconfig  # From the CWD

def main():
    if not os.path.exists("wgbuild"):
        os.mkdir("wgbuild")
    
    generator = Generator(wgconfig.config)
    generator.generate()

if __name__ == "__main__":
    main()
