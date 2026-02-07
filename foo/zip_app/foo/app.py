
from foo import __appname__
from foo import __version__

import click


@click.group
@click.version_option(__version__, prog_name=__appname__)
def main():
    print(f"{__appname__}")


@main.command()
def clone():
    print(f'clone command')


@main.command(help='commit a file')
@click.argument('file')
@click.option('-m', 'message', help='add commit message')
def commit(file, message):
    if message:
        print(f'commit {file} {message}')
    else:
        print(f'commit {file}')
