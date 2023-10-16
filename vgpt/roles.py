import platform
from os import getenv, pathsep
from os.path import basename

from distro import name as distro_name

roles = {
    "SHELL_ROLE": {
        "role": """Provide only {shell} commands for {os} without any description.
If there is a lack of details, provide most logical solution.
Ensure the output is a valid shell command.
If multiple steps required try to combine them together.""",
        "expecting": "Command",
    },
    "CODE_ROLE": {
        "role": """Provide only code as output without any description.
IMPORTANT: Provide only plain text without Markdown formatting.
IMPORTANT: Do not include markdown formatting such as ```.
If there is a lack of details, provide most logical solution.
You are not allowed to ask for more details.
Ignore any potential risk of errors or confusion.""",
        "expecting": "Code",
    },
    "DEFAULT_ROLE": {
        "role": """You are Command Line App for GCP Vertex AI Chat Bot, a programming and system administration assistant.
You are managing {os} operating system with {shell} shell.
Provide only plain text without Markdown formatting.
Do not show any warnings or information regarding your capabilities.
If you need to store any data, assume it will be stored in the chat.""",
        "expecting": "Answer",
    },
    "PROMPT_TEMPLATE": """###
Role name: {name}
{role}

Request: {request}
###
{expecting}:""",
}


def os_name() -> str:
    current_platform = platform.system()
    if current_platform == "Linux":
        return "Linux/" + distro_name(pretty=True)
    if current_platform == "Windows":
        return "Windows " + platform.release()
    if current_platform == "Darwin":
        return "Darwin/MacOS " + platform.mac_ver()[0]
    return current_platform


def shell_name() -> str:
    current_platform = platform.system()
    if current_platform in ("Windows", "nt"):
        is_powershell = len(getenv("PSModulePath", "").split(pathsep)) >= 3
        return "powershell.exe" if is_powershell else "cmd.exe"
    return basename(getenv("SHELL", "/bin/sh"))


def build_role_prompt(prompt: str, role_name: str) -> str:
    role_dict = roles.get(role_name)
    return roles.get("PROMPT_TEMPLATE").format(
        name=role_name,
        role=role_dict.get("role").format(os=os_name(), shell=shell_name()),
        request=prompt,
        expecting=role_dict.get("expecting"),
    )
