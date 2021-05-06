# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import shlex

from colorama import Fore

from pettifogger.workflow.structure.env import Env
from pettifogger.utils.configuration import get_global_configuration


class Step:
    def __init__(self, definition, context, index, parent_job_id, *args, **kwargs):
        self.raw_definition = definition
        self.parent_job_id = parent_job_id
        self.index = index
        self.log_source_id = f"Step {self.index}"
        self.id = definition.get("id")
        setattr(self, "if", definition.get("if"))
        self.name = definition.get("name")
        self.uses = definition.get("uses")
        self.run = definition.get("run")
        setattr(self, "when", definition.get("when"))
        self.continue_on_error = definition.get("continue-on-error")
        self.timeout_minutes = definition.get("timeout-minutes")

        self.env = Env({**context.get("env", {}), **definition.get("env", {})})

        self.configuration = get_global_configuration()

    def __handle_run_step_line_tokens(self, line, logger):
        shlex_instance = shlex.shlex(line, posix=True, punctuation_chars=True)
        script_level_env_var_pairs = []
        command_level_env_var_pairs = []
        has_errors = False
        try:
            token_list = list(shlex_instance)
        except Exception as e:
            has_errors = True
            logger.error(f"Exception: {str(e)} when handling line '{line}'", source_id=self.log_source_id)
            return [], [], has_errors

        i = 0
        while i < len(token_list):
            if token_list[i] == "export":
                m = Env.ENV_VAR_DEFINITION_REGEX.match(token_list[i + 1])
                if m is None:
                    has_errors = True
                    logger.error("Token 'export' was not followed by environment variable definition on line '{line}'",
                                 source_id=self.log_source_id)
                else:
                    script_level_env_var_pairs.append(m.groupdict())
                i += 2
            elif (m := Env.ENV_VAR_DEFINITION_REGEX.match(token_list[i])):
                command_level_env_var_pairs.append(m.groupdict())
            i += 1
        return ({item["key"]: item["value"] for item in script_level_env_var_pairs},
                {item["key"]: item["value"] for item in command_level_env_var_pairs},
                has_errors)

    def __check_run_step_env_vars(self, logger):
        has_errors = False
        has_suspicions = False
        if self.run is not None:
            run_lines = self.run.splitlines()
            script_level_env_vars = {**self.env}
            for line in run_lines:

                new_script_level_env_vars, new_command_level_env_vars, had_errors = \
                    self.__handle_run_step_line_tokens(line, logger)
                if had_errors:
                    has_errors = True

                script_level_env_vars = {**script_level_env_vars, **new_script_level_env_vars}
                command_env_vars = {**script_level_env_vars, **new_command_level_env_vars}

                string_final_env_vars_list = ", ".join(command_env_vars.keys())
                detected_env_vars = Env.ENV_VAR_REGEX.findall(line)
                suspected_env_vars = Env.SUSPECTED_ENV_VARS_REGEX.findall(line)

                for item in detected_env_vars:
                    if item not in command_env_vars:
                        has_errors = True
                        logger.error(
                            f"Could not find variable '{item}' from environment variables ({string_final_env_vars_list}) on line '{line}'",
                            source_id=self.log_source_id
                        )
                    elif str(command_env_vars[item]).strip() == "":
                        has_errors = True
                        logger.error(f"Value of '{item}' is empty on line '{line}'", source_id=self.log_source_id)

                if self.configuration.fail_on_suspicions:
                    suspicion_logger = logger.error
                else:
                    suspicion_logger = logger.warn

                for item in suspected_env_vars:
                    if item not in command_env_vars:
                        has_suspicions = True
                        suspicion_logger(
                            f"Could not find variable '{item}' from environment variables ({string_final_env_vars_list}) on line '{line}'",
                            source_id=self.log_source_id
                        )
                    elif str(command_env_vars[item]).strip() == "":
                        has_suspicions = True
                        suspicion_logger(f"Value of '{item}' is empty on line '{line}'", source_id=self.log_source_id)

        return not has_errors or (self.configuration.fail_on_suspicions and has_suspicions)

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
        logger.info(f"\u2600 Validating step {self.index}:")
        section_logger = logger.new()
        env_var_result = self.__run_validator_and_log(self.__check_run_step_env_vars,
                                                      "Check for undefined environment variables", section_logger)
        result = [
            env_var_result
        ]
        return all(result)