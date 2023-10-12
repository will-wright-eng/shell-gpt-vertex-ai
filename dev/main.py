import os
import json


import typer
import requests
from cachetools import TTLCache

# import google.auth
# import google.auth.transport.requests

# # Obtain the credentials and the request
# credentials, project = google.auth.default()
# auth_req = google.auth.transport.requests.Request()

# # Obtain the token
# credentials.refresh(auth_req)
# token = credentials.token

DEFAULT_CONFIG = {
    "API_ENDPOINT": os.getenv("API_ENDPOINT"),
    "PROJECT_ID": os.getenv("PROJECT_ID"),
    "MODEL_ID": os.getenv("MODEL_ID"),
    # New features might add their own config variables here.
}

# Create a conversation cache with a TTL of 1 hour.
conversation_cache = TTLCache(maxsize=100, ttl=3600)


def export_env_variables_from_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value


def send_prompt(prompt, chat=False):
    # Get an access token.
    # access_token = gcloud.auth.print_access_token()

    # Check if the prompt is already in the conversation cache.
    if prompt in conversation_cache:
        # Return the cached response.
        return conversation_cache[prompt]

    # Create the request body.
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
            "temperature": 0.2,
            "topP": 0.8,
            "topK": 40,
        },
    }

    # Make the request.
    API_ENDPOINT = DEFAULT_CONFIG.get("API_ENDPOINT")
    PROJECT_ID = DEFAULT_CONFIG.get("PROJECT_ID")
    MODEL_ID = DEFAULT_CONFIG.get("MODEL_ID")
    response = requests.post(
        "https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict",
        headers={
            # "Authorization": "Bearer {}".format(access_token),
            "Content-Type": "application/json",
        },
        json=json.dumps(body),
    )

    # Add the response to the conversation cache.
    conversation_cache[prompt] = response.json()

    # Return the response.
    return response.json()


if __name__ == "__main__":
    env_file_path = ".env"
    export_env_variables_from_file(env_file_path)

    app = typer.Typer()

    @app.command()
    def new_conversation(prompt: str):
        """Start a new conversation."""
        send_prompt(prompt)

    @app.command()
    def continue_conversation(prompt: str):
        """Continue an existing conversation."""
        send_prompt(prompt, chat=True)

    app()
