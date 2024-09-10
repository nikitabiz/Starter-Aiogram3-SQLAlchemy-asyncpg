import os

from redis import StrictRedis

redis = StrictRedis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    charset="utf-8",
    decode_responses=True
)