from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str
    debug: bool

    openai_api_key: str
    model_name: str

    class Config:
        env_file = ".env"

settings = Settings()
