#!/bin/env python3

"""
 sslcompare    : compare cipher suites to baselines
 Authors        : Arthur Le Corguille - William Gougam - Alexandre Janvrin
"""
import datetime
import os
import re
import shlex
import subprocess
from functools import partial
from importlib import resources

import click
import yaml

with resources.path("sslcompare", "anssi.yaml") as default_baseline_path:
    DEFAULT_BASELINE_PATH = default_baseline_path


@click.command()
@click.argument("url")
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.option(
    "--baseline", default=DEFAULT_BASELINE_PATH, help="baseline file (yaml)."
)
def main(url, baseline, verbose=False):
    """Scans URL's cipher suites and compares it to the BASELINE

    Cipher suites are retrieved with the testssl.sh shell script
    (https://github.com/drwetter/testssl.sh)

    Examples :
        sslcompare mytargetsite.com -b /path/to/baseline.yaml
    """
    strip_ansi = partial(re.compile(r"\x1b\[\d*m").sub, "")

    with open(baseline) as f:
        baseline_suites = yaml.safe_load(f)

    with resources.as_file(resources.files("sslcompare")) as sslcompare_path:
        with subprocess.Popen(
            shlex.split(
                f"{sslcompare_path / 'testssl.sh/testssl.sh'} -E -U {url}"
            ),
            bufsize=1,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ) as testssl:

            current_protocol = None
            interesting_lines = False

            for line in testssl.stdout:
                line = line.strip()

                if "Start" in line:
                    click.echo(line)

                elif "Done" in line:
                    click.echo(line)
                    break

                elif "Testing" in line:
                    click.echo(line)
                    interesting_lines = True

                elif "Cipher Suite Name (IANA/RFC)" in line:
                    click.echo("Cipher Suite Name (IANA/RFC)")

                elif strip_ansi(line) in [
                    "SSLv2",
                    "SSLv3",
                    "TLS 1",
                    "TLS 1.1",
                    "TLS 1.2",
                    "TLS 1.3",
                ]:
                    current_protocol = strip_ansi(line)
                    click.echo(line)
                    continue

                elif current_protocol is not None and line not in ["", "-"]:
                    cipher_suite = line.split()[-1]
                    try:
                        click.echo(
                            f"{cipher_suite} "
                            + click.style(
                                **baseline_suites[current_protocol][
                                    cipher_suite
                                ]
                            )
                        )
                    except KeyError:
                        click.echo(
                            f"{cipher_suite} "
                            + click.style("[DEPRECATED]", fg="red")
                        )

                elif interesting_lines or verbose:
                    click.echo(line)
