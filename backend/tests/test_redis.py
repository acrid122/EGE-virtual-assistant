import redis
import pytest

def test_redis_connection():
    r = redis.Redis(host="redis", port=6379, db=0)
    r.set("test_key", "test_value")
    assert r.get("test_key").decode() == "test_value"