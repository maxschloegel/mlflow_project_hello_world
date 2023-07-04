import click
from rich.console import Console
from rich.style import Style
console = Console()


@click.command()
@click.argument("name")
def cli(name):
    danger_style = Style(color="red", blink=True, bold=True)
    console.print(f"Danger, {name} Robinson!", style=danger_style)


if __name__ == "__main__":
    cli()
