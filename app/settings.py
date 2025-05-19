from os import getenv
from dotenv import load_dotenv
from pydantic import SecretStr


load_dotenv(".env")


class Settings:
    API_TOKEN: SecretStr = SecretStr(getenv("API_TOKEN"))
    LOGGING_LEVEL: str = getenv("LOGGING_LEVEL")
    API_PORT: int = int(getenv("API_PORT"))
    API_HOST: str = getenv("API_HOST")


SETTINGS = Settings()
