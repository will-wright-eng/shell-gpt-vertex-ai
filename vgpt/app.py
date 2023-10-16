import sys
import json

import typer

from vgpt.gcp import get_session
from vgpt.cache import cache, get_cache_list, get_cache_entry
from vgpt.roles import build_role_prompt
from vgpt.config import Config, config_flow
from vgpt.version import version_callback

# from cachetools import cached, TTLCache


# # Cache with a maximum size of 100 entries and a time-to-live of 300 seconds
# cache = TTLCache(maxsize=100, ttl=300)

# def get_cache_list(cache, chat_session):
#     res = []
#     for chat_session in cache:
#         res.append(chat_session)
#         typer.echo(chat_session)
#     return res

# def get_cache_entry(cache, chat_session):
#     typer.echo(cache[chat_session])


@cached(cache)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        None, "--version", callback=version_callback, help="Show the version and exit.", is_eager=True
    ),
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
    config: bool = typer.Option(
        False,
        help="Config flow for setup and overwite",
        rich_help_panel="Configure CLI",
    ),
    stream: bool = typer.Option(
        True,
        help="Streaming flag",
    ),
    role: str = typer.Option(
        "DEFAULT_ROLE",
        help="System role for GPT model.",
        rich_help_panel="Role Options",
    ),
    cache: bool = typer.Option(
        True,
        help="Cache completion results.",
    ),
    chat: str = typer.Option(
        None,
        help="Follow conversation with id, " 'use "temp" for quick session.',
        rich_help_panel="Chat Options",
    ),
    show_chat: str = typer.Option(
        None,
        help="Show all messages from provided chat id.",
        callback=get_cache_entry,
        rich_help_panel="Chat Options",
    ),
    list_chats: bool = typer.Option(
        False,
        help="List all existing chat ids.",
        callback=get_cache_list,
        rich_help_panel="Chat Options",
    ),
) -> None:
    if config:
        config_flow()
        raise typer.Exit()

    stdin_passed = not sys.stdin.isatty()

    if stdin_passed:
        prompt = f"{prompt or ''}\n---\n{sys.stdin.read()}\n---"

    typer.echo(prompt)

    # if chat and chat not in cache:
    #     prompt = build_role_prompt(prompt, role_name=role)
    #     msg_list = {
    #         "author": "user",
    #         "content": prompt
    #     }
    # elif chat and chat in cache:
    #     msg = {
    #         "author": "user",
    #         "content": prompt
    #     }
    #     msg_list = cache[chat].append(msg)

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
    # TODO: add streaming output
    # https://github.com/TheR1D/shell_gpt/blob/1c585664889e2cfb19ca1e13f0e8d621463ddef3/sgpt/client.py#L59-L78
    response = authed_session.post(
        url,
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps(body),
        stream=stream,
    )
    data = response.json()
    results = data.get("predictions")[0].get("candidates")[0].get("content").strip()
    typer.echo(results)

    # if results and (chat in cache):
    #     msg = {
    #         "author": "bot",
    #         "content": results
    #     }
    #     cache[chat] = msg_list.append(msg)


def entry_point() -> None:
    typer.run(main)


if __name__ == "__main__":
    entry_point()
