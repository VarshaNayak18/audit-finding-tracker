import redis
import json
import os


class CacheService:

    def __init__(self):

        self.client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            decode_responses=True
        )

    def get(self, key):

        data = self.client.get(key)

        if data:
            return json.loads(data)

        return None

    def set(self, key, value):

        self.client.set(
            key,
            json.dumps(value)
        )