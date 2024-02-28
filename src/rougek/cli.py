import click

from rougek.evaluation.commands import evaluate, evaluate_dir
from rougek.extract.commands import extract


@click.group()
def cli():
    pass


cli.add_command(extract)
cli.add_command(evaluate)
cli.add_command(evaluate_dir, name="evaluate_dir")


def main():
    cli()
