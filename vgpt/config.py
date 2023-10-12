import os
from pathlib import Path

import dotenv

from vgpt.log import Log


class Config:
    def __init__(self):
        self.path = Path("~/.config/vgpt").expanduser()
        self.path.mkdir(parents=True, exist_ok=True)
        self.dotenv_path = self.path / "config"
        self.logger = Log()
        self.keys_dict = {
            "API_ENDPOINT": {"name": "API_ENDPOINT", "note": "chat bot endpoint url"},
            "PROJECT_ID": {"name": "PROJECT_ID", "note": "gcp project"},
            "MODEL_ID": {"name": "MODEL_ID", "note": "chat bot model"},
            "GOOGLE_APPLICATION_CREDENTIALS": {"name": "GOOGLE_APPLICATION_CREDENTIALS", "note": "$HOME/.config/gcloud/application_default_credentials.json"},
        }
        self.keys = [ele.get("name") for key, ele in self.keys_dict.items()]
        if not self.check_exists():
            self.logger.error("config file not found")
            self.logger.info(f"check config file exists: {str(self.check_exists())}")
            self.logger.info(f"dotenv_path: {str(self.dotenv_path)}")
            self.configs = None
        else:
            self.configs = self.get_configs()

    def load_env(self):
        dotenv.load_dotenv(dotenv_path=self.dotenv_path)

    def log_current_config(self):
        if self.dotenv_path.is_file():
            with self.dotenv_path.open() as f:
                self.logger.info(f"Current configuration:\n{f.read()}")

    def print_current_config(self):
        if self.dotenv_path.is_file():
            with self.dotenv_path.open() as f:
                print(f"Current configuration:\n{f.read()}")

    def get_configs(self):
        if self.dotenv_path.is_file():
            self.load_env()
            configs = {key: os.getenv(key) for key in self.keys}
        return configs

    def set_key(self, key: str, value: str):
        dotenv.set_key(self.dotenv_path, key, value)

    def update_config(self, atts_dict: dict):
        for key, value in atts_dict.items():
            self.set_key(key, value)

    def check_exists(self):
        return self.dotenv_path.is_file()

    def write_env_vars(self, env_vars: dict):
        with self.dotenv_path.open(mode="a") as f:
            for key, value in env_vars.items():
                f.write(f"{key}={value}\n")
