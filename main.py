import os
import click


@click.command()
@click.argument('name', type=str)
@click.argument('path', default='.', type=click.Path(exists=True))
def main(name, path):
    if os.path.isfile(f"./{name}"):
        print("File Already Exists.")
    else:
        with open(f"./{name}", 'w+') as f:
            pass
        print(f"{name} Created Successfully.")


main()
