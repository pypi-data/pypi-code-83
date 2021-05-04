import sys
from adicity.__main__ import main
def _main():
	argv = ['golfity'] + sys.argv[1:]
	main(argv=argv)
if __name__ == '__main__':
	_main()