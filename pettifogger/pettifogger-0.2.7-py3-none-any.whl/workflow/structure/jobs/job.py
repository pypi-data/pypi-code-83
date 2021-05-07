# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

from colorama import Fore

from pettifogger.utils.configuration import get_global_configuration
from pettifogger.workflow.structure.jobs.container import Container
from pettifogger.workflow.structure.jobs.step import Step
from pettifogger.workflow.structure.jobs.strategy import Strategy
from pettifogger.workflow.structure.env import Env
from pettifogger.workflow.structure.defaults import Defaults


class Job:
    def __init__(self, id, definition, context):
        self.id = id
        self.name = definition.get("name", id)
        self.needs = definition.get("needs")
        self.runs_on = definition.get("runs-on")
        self.permissions = definition.get("permissions")
        self.concurrency = definition.get("concurrency")
        self.outputs = definition.get("outputs")
        setattr(self, "if", definition.get("if"))
        self.timeout_minutes = definition.get("timeout-minutes")

        self.strategy = Strategy(definition.get("strategy")) if "strategy" in definition else None
        self.container = Container(definition.get("container")) if "container" in definition else None
        self.services = Container(definition.get("services")) if "services" in definition else None

        self.env = Env({**context.get("env", {}), **definition.get("env", {})})
        self.defaults = Defaults({**context.get("defaults", {}), **definition.get("defaults", {})})

        self.local_context = {
            "env": {**context.get("env", {}), **definition.get("env", {})},
            "defaults": {**context.get("defaults", {}), **definition.get("defaults", {})},
            "concurrency": definition.get("concurrency", {}),
            "permissions": definition.get("permissions", {})
        }
        self.parent_context = context

        self.context = {
            "env": {**self.parent_context.get("env", {}), **self.local_context.get("env", {})},
            "defaults": {**self.parent_context.get("defaults", {}), **self.local_context.get("defaults", {})},
            "concurrency": {**self.parent_context.get("concurrency", {}), **self.local_context.get("concurrency", {})},
            "permissions": {**self.parent_context.get("permissions", {}), **self.local_context.get("permissions", {})}
        }

        self.steps = [Step(step, self.context, index, self.id) for index, step in enumerate(definition.get("steps", []))]

        self.configuration = get_global_configuration()

    def _has_checkout(self, logger):
        for step in self.steps:
            if step.uses is not None and "actions/checkout@" in step.uses:
                return True
        if self.configuration.fail_on_suspicions:
            suspicion_logger = logger.error
        else:
            suspicion_logger = logger.warn
        suspicion_logger("No checkout", source_id=self.id)

        return False

    def __run_validator_and_log(self, validator, section_name, logger):
        logger.info(f"\u2600 {section_name}:")
        result = validator(logger.new())
        if result:
            logger.info(f"  Result: {Fore.LIGHTGREEN_EX} \u2714")
        else:
            logger.info(f"  Result: {Fore.LIGHTRED_EX} \u2718")
        print()
        return result

    def validate(self, logger):
        logger.info(f"\u2600 Validating job {self.id}:")
        section_logger = logger.new()

        checkout_result = self.__run_validator_and_log(self._has_checkout, "Checking if job has checkout",
                                                       section_logger)

        results = [
            True if not self.configuration.fail_on_suspicions else checkout_result
        ]
        for step in self.steps:
            results.append(step.validate(logger.new()))

        return all(results)