
## models

### chat models

| Model name | Description | Model properties |
| --- | --- | --- |
| chat-bison-32k | Fine-tuned for multi-turn conversation use cases. | Max input and output tokens combined: 32k; Training data: Up to Aug 2023; Max turns : 2500 |
| codechat-bison-32k | A model fine-tuned for chatbot conversations that help with code-related questions. | Max input and output tokens combined: 32k |
| chat-bison | Fine-tuned for multi-turn conversation use cases. | Max input tokens: 8192; Max output tokens: 1024; Training data: Up to Feb 2023; Max turns : 2500 |
| codechat-bison | A model fine-tuned for chatbot conversations that help with code-related questions. | Max input tokens: 6144; Max output tokens: 1024 |

### pre-RLHF models

| Model name | Description | Model properties |
| --- | --- | --- |
| text-bison-32k | Fine-tuned to follow natural language instructions and is suitable for a variety of language tasks. | Max input and output tokens combined: 32k; Training data: Up to Aug 2023 |
| code-bison-32k | A model fine-tuned to generate code based on a natural language description of the desired code. For example, it can generate a unit test for a function. | Max input and output tokens combined: 32k |
| text-bison | Fine-tuned to follow natural language instructions and is suitable for a variety of language tasks, such as: Classification, Sentiment Analysis, Entity extraction, Extractive Question Answering, Summarization, Re-writing text in a different style, Ad copy generation, Concept ideation | Max input tokens: 8192; Max output tokens: 1024; Training data: Up to Feb 2023 |
| textembedding-gecko | Returns model embeddings for text inputs. | 3072 input tokens and outputs 768-dimensional vector embeddings. |
| textembedding-gecko-multilingual | Returns model embeddings for text inputs which support over 100 languages | 3072 input tokens and outputs 768-dimensional vector embeddings. |
| code-bison | A model fine-tuned to generate code based on a natural language description of the desired code. For example, it can generate a unit test for a function. | Max input tokens: 6144; Max output tokens: 1024 |
| code-gecko | A model fine-tuned to suggest code completion based on the context in code that's written. | Max input tokens: 2048; Max output tokens: 64 |

- [Available models in Generative AI Studio | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/models?authuser=1)
- [Reinforcement learning from human feedback - Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)

## initial test env

```bash
conda create -n shell-gpt-vertex-ai python=3.10 -y
conda activate shell-gpt-vertex-ai
python -m pip install jupyterlab google-cloud-aiplatform shapely typer
python -m pip install google-auth google-auth-httplib2

```

## references

- [Vertex AI SDK for Python | Python client library | Google Cloud](https://cloud.google.com/python/docs/reference/aiplatform/latest/index.html)
- [How Application Default Credentials works  |  Authentication  |  Google Cloud](https://cloud.google.com/docs/authentication/application-default-credentials)

## starter code

```bash
API_ENDPOINT="us-central1-aiplatform.googleapis.com"
PROJECT_ID="gpt-development-400805"
MODEL_ID="chat-bison"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict" -d \
$'{
    "instances": [
        {
            "context": "",
            "examples": [],
            "messages": [
                {
                    "author": "user",
                    "content": "hello, can you introduce yourself?"
                },
                {
                    "content": " I am a large language model, trained by Google.",
                    "author": "bot",
                    "citationMetadata": {
                        "citations": []
                    }
                },
                {
                    "author": "user",
                    "content": "can you help me with programming?"
                },
                {
                    "author": "bot",
                    "content": " I can help you with programming. What kind of help do you need?
",
                    "citationMetadata": {
                        "citations": []
                    }
                },
                {
                    "author": "user",
                    "content": "I\'m trying to create a command line interface for the vertex chat api. I\'d like this cli to be written in python with the module typer. can you give me boilerplate code?"
                },
                {
                    "author": "bot",
                    "content": " ```python
import typer

app = typer.Typer()


@app.command()
def create_user(username: str, password: str):
    \\"\\"\\"Create a new user.\\"\\"\\"
    # TODO: Implement user creation.


@app.command()
def get_user(username: str):
    \\"\\"\\"Get a user by username.\\"\\"\\"
    # TODO: Implement user retrieval.


@app.command()
def update_user(username: str, new_username: str, new_password: str):
    \\"\\"\\"Update a user\'s username and password.\\"\\"\\"
    # TODO: Implement user update.


@app.command()
def delete_user(username: str):
    \\"\\"\\"Delete a user.\\"\\"\\"
    # TODO: Implement user deletion.


if __name__ == \\"__main__\\":
    app()
```",
                    "citationMetadata": {
                        "citations": []
                    }
                },
                {
                    "author": "user",
                    "content": "rather than a crud application, can you modify the boilerplate to send prompts to the vertex api endpoint -- similar to this curl commands:

```bash
API_ENDPOINT=\\"us-central1-aiplatform.googleapis.com\\"
PROJECT_ID=\\"gpt-development-400805\\"
MODEL_ID=\\"chat-bison\\"

curl \\\\
-X POST \\\\
-H \\"Authorization: Bearer $(gcloud auth print-access-token)\\" \\\\
-H \\"Content-Type: application/json\\" \\\\
\\"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict\\" -d \\\\
$\'{
    \\"instances\\": [
        {
            \\"context\\": \\"\\",
            \\"examples\\": [],
            \\"messages\\": [
                {
                    \\"author\\": \\"user\\",
                    \\"content\\": \\"hello, can you introduce yourself?\\"
                },
                {
                    \\"content\\": \\" I am a large language model, trained by Google.\\",
                    \\"author\\": \\"bot\\",
                    \\"citationMetadata\\": {
                        \\"citations\\": []
                    }
                },
                {
                    \\"author\\": \\"user\\",
                    \\"content\\": \\"can you help me with programming?\\"
                },
                {
                    \\"author\\": \\"bot\\",
                    \\"content\\": \\" I can help you with programming. What kind of help do you need?
\\",
                    \\"citationMetadata\\": {
                        \\"citations\\": []
                    }
                },
                {
                    \\"author\\": \\"user\\",
                    \\"content\\": \\"I\\\\\'m trying to create a command line interface for the vertex chat api. I\\\\\'d like this cli to be written in python with the module typer. can you give me boilerplate code?\\"
                }
            ]
        }
    ],
    \\"parameters\\": {
        \\"candidateCount\\": 1,
        \\"maxOutputTokens\\": 256,
        \\"temperature\\": 0.2,
        \\"topP\\": 0.8,
        \\"topK\\": 40
    }
}\'
```"
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
}'
```
