import pytest
from typer.testing import CliRunner
from vgpt.app import app

runner = CliRunner()


@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_hello_command(name):
    result = runner.invoke(app, ["hello", name])
    assert result.exit_code == 0
    assert f"Hello, {name.title()}!" in result.output


@pytest.mark.parametrize(
    "prompt, temperature, top_probability, cache, role",
    [
        ("Hello", 0.5, 0.9, True, "admin"),
        ("How are you?", 0.3, 0.8, False, "user"),
    ],
)
def test_send_command(prompt, temperature, top_probability, cache, role):
    result = runner.invoke(
        app,
        [
            "send",
            "--prompt",
            prompt,
            "--temperature",
            str(temperature),
            "--top-probability",
            str(top_probability),
            "--cache",
            str(cache),
            "--role",
            role,
        ],
    )
    assert result.exit_code == 0
    # Add assertions for the expected output


def test_config_test_command():
    result = runner.invoke(app, ["config_test"])
    assert result.exit_code == 0
    # Add assertions for the expected output


def test_config_command():
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
    # Add assertions for the expected output
