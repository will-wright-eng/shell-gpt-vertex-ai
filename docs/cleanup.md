# cleanup

## tests

- [Get Started — pytest documentation](https://docs.pytest.org/en/7.1.x/getting-started.html)
- add hello test to cookiecutter template
    - [will-wright-eng/cookiecutter-typer-cli: cookiecutter template for Typer command line interface](https://github.com/will-wright-eng/cookiecutter-typer-cli)

## app

- remove hello command
- add cache module
- add roles module
- role all endpoints into main()
- [shell_gpt/sgpt/app.py at main · TheR1D/shell_gpt](https://github.com/TheR1D/shell_gpt/blob/main/sgpt/app.py)

```py
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
    )
) -> None:
```

## flake8

```bash
flake8..........Passed
- hook id: flake8
- duration: 0.5s

vgpt/app.py:1:1: F401 'os' imported but unused
vgpt/app.py:4:1: F401 'typing.Optional' imported but unused
vgpt/app.py:5:1: F401 'pathlib.Path' imported but unused
vgpt/app.py:31:21: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:52:19: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:57:26: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:63:30: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:69:19: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:73:17: B008 Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the result of that definition-time function call.  If this is intended, assign the function call to a module-level variable and use that variable as a default value.
vgpt/app.py:113:13: F541 f-string is missing placeholders
vgpt/app.py:140:9: F841 local variable 'key_name' is assigned to but never used
vgpt/app.py:141:9: F841 local variable 'key_note' is assigned to but never used
```
