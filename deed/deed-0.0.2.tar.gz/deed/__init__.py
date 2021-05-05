from enum import Enum, auto
import logging
import sys
import time

import json

from deed import audit_modes


logger = logging.getLogger('auditlog')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class AuditMode(Enum):
    DIFF = 'diff'
    PREV_AND_NEW = 'prev_and_new'
    JSON_PATCH = 'jsonpatch'  # RFC-6902  https://tools.ietf.org/html/rfc6902

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v

    def new_builder(self, audit_log):
        return audit_modes.get_builder(self.value)(audit_log)


class AuditLog:

    def __init__(self, resource_type, action, audit_mode: AuditMode = AuditMode.DIFF):
        self.resource_type = resource_type
        self.action = action
        self.audit_mode = audit_mode.value
        self.actor: str = 'unknown'
        self.where: str = 'unknown'
        self.stakeholders: list = []
        self.channel: str = 'default'

    def session(self, actor, stakeholders: list = None, channel=None, where=None):
        self.actor = actor
        if stakeholders is not None:
            self.stakeholders = stakeholders
        self.channel = channel or self.channel
        self.where = where or self.where

    def audit(self, resource, payload=None, **kwargs):
        # TODO: check session requisites
        # build changes (diff or prev_and_new modes)
        mode = AuditMode.value_of(self.audit_mode)
        complement = mode.new_builder(self).build(resource, payload)
        # flush audit_log to STDOUT (or another stream)
        if complement is not None:
            complement['when'] = int(time.time())
            audited_result = {**self.__dict__, **complement}
            kwargs['resource_ref'] = resource.get('_id') or resource.get('id')
            audited_result.update({k: v for k, v in kwargs.items() if v})
            logger.info(json.dumps(audited_result, separators=[',', ':']))
            return audited_result
