import redis

with redis.Redis() as redis_server:
    redis_server.lpush("gueue", 10, 10, 20, 30)
