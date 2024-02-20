import sys

import click


@click.command()
@click.argument("file", type=click.File("r", "utf-8"), required=False)
def nl(file):
    if file is None:
        file = sys.stdin
    for i, line in enumerate(file, 1):
        print(f"{i}\t{line}", end="")


if __name__ == "__main__":
    nl()
