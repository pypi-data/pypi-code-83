from .state.generator import Generator
from .state.loader import Loader
from .user.cli import parse_cli
from .user.reporter import Reporter


def main() -> None:
    inputs, flags = parse_cli()

    reporter = Reporter(flags)
    reporter.launch()

    loader = Loader(inputs)
    reporter.show_loader(loader)
    loader.introspect()

    generator = Generator(flags, loader, reporter)
    generator.sequence()


if __name__ == "__main__":
    main()
