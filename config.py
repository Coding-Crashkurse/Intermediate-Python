from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: str = 6379
    db: int = 0
    password: str = "test"
    decode_responses: bool = True
