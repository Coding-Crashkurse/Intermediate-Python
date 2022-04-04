import redis

from config import Settings

settings = Settings()
database = redis.Redis(**settings.dict())
