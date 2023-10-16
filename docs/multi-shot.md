# few shot training

## install

`gcloud auth application-default login`

## bash

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
                    "content": "tell me who you are"
                },
                {
                    "author": "bot",
                    "content": " I am a large language model, trained by Google.
",
                    "citationMetadata": {
                        "citations": []
                    }
                },
                {
                    "author": "user",
                    "content": "what can you do?"
                }
            ]
        }
    ],
    "parameters": {
        "candidateCount": 1,
        "maxOutputTokens": 1024,
        "temperature": 0.2,
        "topP": 0.8,
        "topK": 40
    }
}'
```
