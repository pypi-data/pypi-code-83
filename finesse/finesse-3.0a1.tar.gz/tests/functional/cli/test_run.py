"""CLI run command tests."""

from tempfile import NamedTemporaryFile
from finesse.__main__ import run
from finesse.script import parse_file
from .util import sanitized_output


def test_run_same_as_python_api(isolated_cli, input_file):
    """Test that running kat script via CLI same as calling :meth:`finesse.script.parse_file`."""
    cli_result = isolated_cli.invoke(run, [input_file.name, "--no-plot"])

    api_model = parse_file(input_file.name)
    api_solution = api_model.run()

    assert str(api_solution) in sanitized_output(cli_result)
    assert cli_result.exit_code == 0


def test_trace_flag(isolated_cli, input_file):
    """Test the --trace run flag."""
    cli_result = isolated_cli.invoke(run, [input_file.name, "--no-plot", "--trace"])
    assert "Trace:" in sanitized_output(cli_result)
    assert cli_result.exit_code == 0


def test_no_trace_flag(isolated_cli, input_file):
    """Test the --trace run flag."""
    cli_result = isolated_cli.invoke(run, [input_file.name, "--no-plot", "--no-trace"])
    assert "Trace:" not in sanitized_output(cli_result)
    assert cli_result.exit_code == 0


def test_parse_error(isolated_cli):
    """Test that parsing errors appear in the output."""
    with NamedTemporaryFile("r+") as fobj:
        fobj.write("laser l1 __fake_param__=1")
        fobj.flush()
        cli_result = isolated_cli.invoke(run, [fobj.name, "--no-plot"])
        assert "ERROR:" in sanitized_output(cli_result)
        assert cli_result.exit_code > 0
