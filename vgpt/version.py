import toml
import typer


def get_version():
    pyproject = toml.load("pyproject.toml")
    return pyproject["tool"]["poetry"]["version"]


def version_callback(value: bool):
    if value:
        typer.echo(f"VGPT CLI Version: {get_version()}")
        raise typer.Exit()
