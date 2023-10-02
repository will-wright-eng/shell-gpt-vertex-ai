import typer
import requests
from cachetools import TTLCache

API_ENDPOINT = "us-central1-aiplatform.googleapis.com"
PROJECT_ID = "gpt-development-400805"
MODEL_ID = "chat-bison"

# Create a conversation cache with a TTL of 1 hour.
conversation_cache = TTLCache(maxsize=100, ttl=3600)

def send_prompt(prompt, chat=False):
  # Get an access token.
  access_token = gcloud.auth.print_access_token()

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
              "messages": [
                  {
                      "author": "user",
                      "content": prompt
                  }
              ]
          }
      ],
      "parameters": {
          "candidateCount": 1,
          "maxOutputTokens": 256,
          "temperature": 0.2,
          "topP": 0.8,
          "topK": 40
      }
  }

  # Make the request.
  response = requests.post(
      "https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict",
      headers={
          "Authorization": "Bearer {}".format(access_token),
          "Content-Type": "application/json",
      },
      json=body,
  )

  # Add the response to the conversation cache.
  conversation_cache[prompt] = response.json()

  # Return the response.
  return response.json()

if __name__ == "__main__":
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
