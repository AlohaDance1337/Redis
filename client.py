import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop("gueue")

print(int(value[1]))