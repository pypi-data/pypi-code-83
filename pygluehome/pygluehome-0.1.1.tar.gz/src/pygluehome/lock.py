from datetime import datetime
from enum import Enum
import iso8601


class GlueHomeLock:
    def __init__(self, api, lock_id, data):
        """
        :type api: pygluehome.api.GlueHomeApi
        """
        self._api = api
        self.lock_id = lock_id
        self._data = data
        self.updated_at = datetime.now()

    @property
    def serial_number(self):
        return self._data['serialNumber']

    @property
    def description(self):
        return self._data['description']

    @property
    def firmware_version(self):
        return self._data['firmwareVersion']

    @property
    def battery_status(self):
        return self._data['batteryStatus']

    @property
    def connection_status(self):
        return GlueHomeLockConnectionStatus(self._data['connectionStatus'])

    @property
    def last_lock_event(self):
        if self._data['lastLockEvent']:
            return GlueHomeLockEvent(
                GlueHomeLockEventType(self._data['lastLockEvent']['eventType']),
                iso8601.parse_date(self._data['lastLockEvent']['eventTime'])
            )

        return None

    @property
    def model(self):
        return self.serial_number[:4]

    @property
    def is_battery_low(self):
        return self.battery_status < 50

    def __repr__(self):
        return f'GlueHomeLock[id={self.lock_id}, data={str(self._data)}, updated={str(self.updated_at)}]'

    async def refresh(self):
        self._data = await self._api._lock_data(self.lock_id)
        self.updated_at = datetime.now()

    async def lock(self):
        await self._api._lock_lock(self.lock_id)
        await self.refresh()

    async def unlock(self):
        await self._api._unlock_lock(self.lock_id)
        await self.refresh()


class GlueHomeLockConnectionStatus(Enum):
    offline = 'offline'
    disconnected = 'disconnected'
    connected = 'connected'
    busy = 'busy'


class GlueHomeLockEventType(Enum):
    unknown = 'unknown'
    local_lock = 'localLock'
    local_unlock = 'localUnlock'
    remote_lock = 'remoteLock'
    remote_unlock = 'remoteUnlock'
    press_and_go = 'pressAndGo'
    manual_unlock = 'manualUnlock'
    manual_lock = 'manualLock'


class GlueHomeLockEvent:
    def __init__(self, event_type: GlueHomeLockEventType, datetime):
        self.event_type = event_type
        self.datetime = datetime