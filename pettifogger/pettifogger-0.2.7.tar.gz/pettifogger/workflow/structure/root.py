# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import json
import os

import networkx as nx
from jsonschema import Draft7Validator
from colorama import Fore, Style

from .defaults import Defaults
from .env import Env
from .jobs.job import Job
from .on import On


class Workflow:
    def __init__(self, definition):
        self.raw_definition = definition

        self.name = definition.get("name", "Unnamed workflow")
        self.permissions = definition.get("permissions")
        self.concurrency = definition.get("concurrency")

        self.on = On(definition.get("on"))
        self.env = Env(definition.get("env")) if "env" in definition else None
        self.defaults = Defaults(definition.get("defaults")) if "defaults" in definition else None

        context = {
            "env": definition.get("env", {}),
            "defaults": definition.get("defaults", {}),
            "concurrency": definition.get("concurrency", {}),
            "permissions": definition.get("permissions", {})
        }

        self.jobs = [Job(id, definition, context) for id, definition in definition.get("jobs", {}).items()]

    def __forms_dag(self, logger):
        nodes = [ job.id for job in self.jobs ]
        edges = [(origin, target.id) for target in self.jobs if target.needs is not None for origin in target.needs ]

        G = nx.MultiDiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        is_dag = nx.algorithms.dag.is_directed_acyclic_graph(G)

        if not is_dag:
            logger.error("The workflow jobs do not form a directed acyclic graph", source_id=self.name)

        return is_dag

    def __jobs_have_no_undefined_needs(self, logger):
        job_names = [job.id for job in self.jobs]
        jobs_with_needs = [job for job in self.jobs if job.needs is not None]

        for job in jobs_with_needs:
            for need in job.needs:
                if need not in job_names:
                    logger.error(f"Undefined need ({need}) in job {job.id}", source_id=job.id)


    def __validate_schema(self, logger):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "utils", "schema.json")) as schema_file:
            __schema = json.load(schema_file)

        validator = Draft7Validator(__schema)
        valid = validator.is_valid(dict(self.raw_definition))
        for error in validator.iter_errors(dict(self.raw_definition)):
            logger.error(f"{error.message} (path: {'.'.join(error.path)})", source_id=f"{self.name} - schema")
        return valid

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
        logger.info(f"\u2600 Workflow: {self.name}")
        section_logger = logger.new()
        schema_result = self.__run_validator_and_log(self.__validate_schema, "Schema validation", section_logger)

        dag_result = self.__run_validator_and_log(self.__forms_dag, "Check that jobs for a directed acyclic graph",
                                                  section_logger)

        no_undefined_needs_result = self.__run_validator_and_log(self.__jobs_have_no_undefined_needs,
                                                                 "Check for undefined needs", section_logger)

        results = [
            schema_result,
            dag_result,
            no_undefined_needs_result
        ]

        section_logger.info("\u2600 Validating jobs:")
        for job in self.jobs:
            results.append(job.validate(section_logger.new()))
            print()
        return all(results)