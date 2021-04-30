from rnnoise_cli import rnnoise
from click.testing import CliRunner

if __name__ == '__main__':
    runner = CliRunner()
    result = runner.invoke(rnnoise, ["activate"])
