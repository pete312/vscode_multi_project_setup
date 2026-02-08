
from bar import __appname__
from pathlib import Path
import click

@click.group
def main():
    print(f"{__appname__}")


@main.command()
@click.argument('files', nargs=-1)
@click.option('-h', '--header', is_flag=True, help="print out the file as a header")
def cat(files:list[str], header:bool):
    for file in files:
        if header:
            print(f' ========={file}=========')
        print(Path(file).read_text())
