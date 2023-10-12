import os
import sys
import json
from typing import Optional
from pathlib import Path

import toml
import typer
from typer import echo

from vgpt.gcp import get_session
from vgpt.config import Config

app = typer.Typer(add_completion=False)


def get_version():
    pyproject = toml.load("pyproject.toml")
    return pyproject["tool"]["poetry"]["version"]


def version_callback(value: bool):
    if value:
        print(f"VGPT CLI Version: {get_version()}")
        raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(
        None, "--version", callback=version_callback, help="Show the version and exit.", is_eager=True
    ),
):
    pass


@app.command()
def hello(name: str) -> None:
    """
    first endpoint
    """
    print(f"Hello, {name.title()}!")


@app.command()
def send(
    prompt: str = typer.Argument(
        None,
        show_default=False,
        help="The prompt to generate completions for.",
    ),
    temperature: float = typer.Option(
        0.2,
        min=0.0,
        max=2.0,
        help="Randomness of generated output.",
    ),
    top_probability: float = typer.Option(
        0.8,
        min=0.1,
        max=1.0,
        help="Limits highest probable tokens (words).",
    ),
    cache: bool = typer.Option(
        True,
        help="Cache completion results.",
    ),
    role: str = typer.Option(
        None,
        help="System role for GPT model.",
        rich_help_panel="Role Options",
    ),
) -> None:
    stdin_passed = not sys.stdin.isatty()

    if stdin_passed:
        prompt = f"{prompt or ''}\n---\n{sys.stdin.read()}\n---"

    print(prompt)
    body = {
        "instances": [
            {
                "context": "",
                "examples": [],
                "messages": [{"author": "user", "content": prompt}],
            }
        ],
        "parameters": {
            "candidateCount": 1,
            "maxOutputTokens": 256,
            "temperature": temperature,
            "topP": top_probability,
            "topK": 40,
        },
    }
    configs = Config().get_configs()
    API_ENDPOINT = configs.get("API_ENDPOINT")
    PROJECT_ID = configs.get("PROJECT_ID")
    MODEL_ID = configs.get("MODEL_ID")
    authed_session = get_session()
    url = f"https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict"
    response = authed_session.post(
        url,
        headers={
            f"Authorization": "Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(body),
    )
    print(json.dumps(response.json(), indent=2))


@app.command()
def config_test() -> None:
    """
    config test endpoint
    """

    configs = Config().get_configs()
    print(f"configs:\n{json.dumps(configs, indent=2)}")
    return


def write_config(config):
    config.dotenv_path.unlink(missing_ok=True)
    config.dotenv_path.touch()
    echo()
    env_vars = {}
    config_dict = config.configs

    for key, val in config.keys_dict.items():
        key_name = val.get("name")
        key_note = val.get("note")

        if config_dict:
            res_default = config_dict.get(key)
        else:
            res_default = None

        res = typer.prompt(f"{key} ({val.get('note')})", type=str, default=res_default)
        env_vars[key] = res

    config.write_env_vars(env_vars)
    config.print_current_config()


@app.command()
def config() -> None:
    """
    Configures the application
    """
    config = Config()

    if config.check_exists():
        config.load_env()
        config.print_current_config()

        if typer.confirm("Would you like to overwrite these settings?", default=False):
            echo("Overwriting")
            write_config(config)
    else:
        write_config(config)

    echo("Configuration complete.")


def entry_point() -> None:
    app()


if __name__ == "__main__":
    entry_point()
