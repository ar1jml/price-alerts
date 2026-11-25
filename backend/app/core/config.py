from pathlib import Path

from dotenv import load_dotenv

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


def load_environment() -> None:
    load_dotenv(ENV_FILE)