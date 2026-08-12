from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    debug: bool = False
    database_url: str
    APP_NAME: str = "Famsure"
    ASYNC_DATABASE_URL: str
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
