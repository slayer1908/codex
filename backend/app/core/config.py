from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ApexAds Autonomous AI Marketing OS"
    environment: str = "development"
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/apexads"
    redis_url: str = "redis://redis:6379/0"
    openai_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_index: str = "apexads-marketing"
    google_ads_developer_token: str = ""
    google_ads_client_id: str = ""
    google_ads_client_secret: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
