from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: str = 6379
    db: int = 0
    password: str = "eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81"
    decode_responses: bool = False
