from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_webhook_secret = ""

    class config:
        env_file = ".env"