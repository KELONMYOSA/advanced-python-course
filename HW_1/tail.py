import sys

import click


@click.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def tail(files):
    if not files:
        files = [None]

    for file in files:
        try:
            if len(files) > 1:
                print(f"==> {file} <==")

            if file:
                with open(file, encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines[-10:]:
                        print(line, end="")
                    print()
            else:
                content = sys.stdin.read()
                lines = content.splitlines()
                for line in lines[-17:]:
                    print(line)
        except Exception as e:
            print(f"Error reading {file}: {e}")


if __name__ == "__main__":
    tail()
