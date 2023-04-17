import click
from rougek import extract


@click.group()
def cli():
    pass

cli.add_command(extract)

def main():
    cli()
