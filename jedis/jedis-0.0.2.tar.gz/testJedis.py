from Jedis import jedis

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

j.dset("myDict", "name", "kobsser")     # to set dictionary.                                    in redis: hset
j.set("age", 12)                        # to set key ``name`` to ``value``                      in redis: set
j.get("age")                            # to get value of the ``name``                          in redis: get
j.delete("age", "name", "lastName")     # to delete an or more key                              in redis: delete
j.exists("age")                         # to check if ``name`` exists                           in redis: exists
j.lpush("myList", 16, True, "kobsser")  # to push values onto the head of list ``name``         in redis: lpush
j.lrange("myList", 0, 5)                # Return a slice of list between position start - end   in redis: lrange
# ...
