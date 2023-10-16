# Shell GPT Vertex AI

[![PyPI](https://img.shields.io/pypi/v/vgpt)](https://pypi.org/project/vgpt/)
[![Downloads](https://static.pepy.tech/badge/vgpt/month)](https://pepy.tech/project/vgpt)
[![Supported Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.org/project/vgpt/)
[![Contributors](https://img.shields.io/github/contributors/will-wright-eng/shell-gpt-vertex-ai.svg)](https://github.com/will-wright-eng/shell-gpt-vertex-ai/graphs/contributors)
[![Tests](https://github.com/will-wright-eng/shell-gpt-vertex-ai/workflows/Test/badge.svg)](https://github.com/will-wright-eng/shell-gpt-vertex-ai/actions?query=workflow%3ATest)

## Summary

**a command line interface for google cloud platform' 's vertex ai chat bot**

- generated using: [will-wright-eng/cookiecutter-typer-cli](https://github.com/will-wright-eng/cookiecutter-typer-cli)

## Installing `vgpt` & Supported Versions

`vgpt` is available on PyPI:

```bash
python -m pip install vgpt
```

Shell GPT Vertex AI Command Line Interface officially supports Python 3.8+.

## Supported Features & Usage

For help, run:

```bash
vgpt --help
```

Commands:

```bash
➜ vgpt --help

 Usage: vgpt [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  config       Configures the application
  config-test  config test endpoint
  hello        first endpoint
```

## Development

To contribute to this tool, first checkout the code:

```bash
git clone https://github.com/will-wright-eng/shell-gpt-vertex-ai.git
cd shell-gpt-vertex-ai
```

Then create a new virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```

Install pre-commit before submitting a PR:

```bash
brew install pre-commit
pre-commit install
```

## References

- [PyPI Package](https://pypi.org/project/vgpt)
- Based on cookiecutter template [will-wright-eng/click-app](https://github.com/will-wright-eng/click-app)
