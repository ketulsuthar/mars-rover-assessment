import os
import click
from mars_rover import app


@click.command()
@click.option('--filename', help='Input file.')
def cli(filename):
    if os.path.exists(filename):
        app.main(filename)
    else:
        print('file does not exist.')

