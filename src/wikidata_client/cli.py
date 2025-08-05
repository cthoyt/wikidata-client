"""Command line interface for :mod:`wikidata_client`."""

import click

__all__ = [
    "main",
]


@click.command()
@click.option("--name", required=True, help="The name of the person to say hello to")
def main(name: str) -> None:
    """CLI for wikidata_client."""
    click.echo("Hello from the CLI!")


if __name__ == "__main__":
    main()
