import pytest
import click
from click.testing import CliRunner

from pcli import cli
from paws import __version__

@pytest.fixture
def runner():
	cli_runner = CliRunner()
	yield cli_runner

# Can add other tests such as running the actual download command...
def test_cli(runner):
	result = runner.invoke(cli, ["--version"])

	assert __version__ in result.output