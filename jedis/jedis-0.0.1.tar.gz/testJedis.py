
import redis
from jedis import jedis
# info: hset -> name, key, value
# info: hget -> name, key
# info: hdel -> name, *keys
# info: hkeys -> name
# info: hlen -> name
# info: hgetall -> name
# info: hexists -> name, key
# info: type -> name
# info: exists -> name
# sep ------ lists ------
# info: lpush -> name, *values
# info: rpush -> name, *values
# info: lrange -> name, start, end
# info: llen -> name
# info: lrem -> name, count, value

j = jedis("kobs.json")

# TODO: add functions below
# redis.Redis.lset() info: ok
# redis.Redis.lrem() info: ok
# redis.Redis.lindex() info: ok

print(j.lrange("l"))
