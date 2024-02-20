import sys

import click


@click.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def wc(files):
    total_lines, total_words, total_bytes = 0, 0, 0
    for file in files:
        try:
            with open(file, encoding="utf-8") as f:
                lines = f.readlines()
                words, bytes_ = 0, 0
                for line in lines:
                    words += len(line.split())
                    bytes_ += len(line.encode("utf-8"))

                print(f"{len(lines)} {words} {bytes_} {file}")
                total_lines += len(lines)
                total_words += words
                total_bytes += bytes_
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if len(files) > 1:
        print(f"{total_lines} {total_words} {total_bytes} total")
    elif len(files) == 0:
        content = sys.stdin.read()
        lines = content.splitlines()
        words = len(content.split())
        bytes_ = len(content.encode("utf-8"))
        print(f"{len(lines)} {words} {bytes_}")


if __name__ == "__main__":
    wc()
