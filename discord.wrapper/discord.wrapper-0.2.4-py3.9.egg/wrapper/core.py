import datetime
from abc import ABC

class Snowflake(ABC):
    DISCORD_EPOCH = 1420070400000
    
    @property
    def created_at(self):
        timestamp = ((self.id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)    