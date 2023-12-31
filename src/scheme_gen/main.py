import click

import scheme_gen.__init__ as init
from scheme_gen.hello_world import say_hi


@click.group()
def cli():
    """OKP4 python template, program description."""
    pass


@cli.command
def version():
    """Print the application version information"""
    click.echo(init.__version__)


@cli.command
@click.option(
    "-n",
    "--name",
    "name",
    type=str,
    required=False,
    default="friend",
    help="A name to salute",
)
def main_cmd(name: str):
    """Does something interesting..."""
    say_hi(name)


if __name__ == "__main__":
    cli()
