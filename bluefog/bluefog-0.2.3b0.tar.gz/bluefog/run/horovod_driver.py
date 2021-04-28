
# Modifications copyright (C) 2020 Bluefog Team. All Rights Reserved.
# Copyright 2019 Uber Technologies, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
import sys

import six
from bluefog.run.horovodrun.common.util import codec, safe_shell_exec, timeout, secret
from bluefog.run.horovodrun.driver import driver_service
from bluefog.run.horovodrun.task import task_service
from bluefog.run.horovodrun.util import threads


def _launch_task_servers(all_host_names, local_host_names, driver_addresses,
                         num_hosts, tmout,
                         key, ssh_port=None):
    """
    executes the task server and service client task for registration on the
    hosts.
    :param all_host_names: list of addresses. for example,
        ['worker-0','worker-1']
        ['10.11.11.11', '10.11.11.12']
    :type all_host_names: list(string)
    :param local_host_names: names that are resolved to one of the addresses
    of local hosts interfaces. For example,
        set(['localhost', '127.0.0.1'])
    :type local_host_names: set
    :param driver_addresses: map of interfaces and their address and port for
    the service. For example:
        {
            'lo': [('127.0.0.1', 34588)],
            'docker0': [('172.122.10.1', 34588)],
            'eth0': [('11.111.33.73', 34588)]
        }
    :type driver_addresses: map
    :param num_hosts:
    :type num_hosts: int
    :param tmout:
    :type tmout: horovod.spark.util.timeout.Timeout
    :return:
    :rtype:
    """

    def _exec_command(command):
        host_output = six.StringIO()
        try:
            exit_code = safe_shell_exec.execute(command,
                                                stdout=host_output,
                                                stderr=host_output)
            if exit_code != 0:
                print(
                    "Launching bluefog task function was not "
                    "successful:\n{host_output}"
                    .format(host_output=host_output.getvalue()))
                os._exit(exit_code)
        finally:
            host_output.close()
        return exit_code

    if ssh_port:
        ssh_port_arg = "-p {ssh_port}".format(ssh_port=ssh_port)
    else:
        ssh_port_arg = ""

    args_list = []
    for index, host_name in enumerate(all_host_names):
        if host_name in local_host_names:
            command = \
                '{python} -m bluefog.run.horovodrun.task_fn {index} ' \
                '{driver_addresses} {num_hosts} {timeout} {key}'.format(
                    python=sys.executable,
                    index=codec.dumps_base64(index),
                    driver_addresses=codec.dumps_base64(driver_addresses),
                    num_hosts=codec.dumps_base64(num_hosts),
                    timeout=codec.dumps_base64(tmout),
                    key=codec.dumps_base64(key)
                )
        else:
            command = \
                'ssh -o StrictHostKeyChecking=no {host} {ssh_port_arg} ' \
                '\'{python} -m bluefog.run.horovodrun.task_fn {index} ' \
                '{driver_addresses} {num_hosts} {timeout} {key}\''.format(
                    host=host_name,
                    ssh_port_arg=ssh_port_arg,
                    python=sys.executable,
                    index=codec.dumps_base64(index),
                    driver_addresses=codec.dumps_base64(driver_addresses),
                    num_hosts=codec.dumps_base64(num_hosts),
                    timeout=codec.dumps_base64(tmout),
                    key=codec.dumps_base64(key)
                )
        args_list.append([command])
    # Each thread will use ssh command to launch the server on one task. If an
    # error occurs in one thread, entire process will be terminated. Otherwise,
    # threads will keep running and ssh session -- and the the task server --
    # will be bound to the thread. In case, the horovodrun process dies, all
    # the ssh sessions and all the task servers will die as well.
    threads.execute_function_multithreaded(_exec_command,
                                           args_list,
                                           block_until_all_done=False)


def driver_fn(all_host_names, local_host_names, ssh_port=None,
              verbose=False):
    """
    launches the service service, launches the task service on each worker and
    have them register with the service service. Each worker probes all the
    interfaces of the worker index + 1 (in a ring manner) and only keeps the
    routed interfaces. Function returns the intersection of the set of all the
    routed interfaces on all the workers.
    :param all_host_names: list of addresses. for example,
        ['worker-0','worker-1']
        ['10.11.11.11', '10.11.11.12']
    :type all_host_names: list(string)
    :param local_host_names: host names that resolve into a local addresses.
    :type local_host_names: set
    :param tmout:
    :type tmout: horovod.spark.util.timeout.Timeout
    :param verbose:
    :type verbose: bool
    :return: example: ['eth0', 'eth1']
    :rtype: list[string]
    """
    key = secret.make_secret_key()
    tmout = timeout.Timeout(int(os.getenv('BLUEFOG_START_TIMEOUT', '600')))
    num_hosts = len(all_host_names)
    # Launch a TCP server called service service on the host running bluefogrun.
    driver = driver_service.HorovodRunDriverService(num_hosts, key)
    if verbose:
        print("Launched bluefog run server.")
    # Have all the workers register themselves with the service service.
    _launch_task_servers(all_host_names, local_host_names,
                         driver.addresses(), num_hosts, tmout,
                         key, ssh_port)
    if verbose:
        print("Attempted to launch bluefog task servers.")
    try:
        # wait for all the hosts to register with the service service.
        if verbose:
            print("Waiting for the hosts to acknowledge.")
        driver.wait_for_initial_registration(tmout)
        tasks = [task_service.HorovodRunTaskClient(index,
                                                   driver.task_addresses_for_driver(
                                                       index),
                                                   key)
                 for index in range(num_hosts)]
        # Notify all the drivers that the initial registration is complete.
        for task in tasks:
            task.notify_initial_registration_complete()
        if verbose:
            print("Notified all the hosts that the registration is complete.")
        # Each worker should probe the interfaces of the next worker in a ring
        # manner and filter only the routed ones -- it should filter out
        # interfaces that are not really connected to any external networks
        # such as lo0 with address 127.0.0.1.
        if verbose:
            print("Waiting for hosts to perform host-to-host "
                  "interface checking.")
        driver.wait_for_task_to_task_address_updates(tmout)
        if verbose:
            print("Host-to-host interface checking successful.")
        # Determine a set of common interfaces for task-to-task communication.
        common_intfs = set(driver.task_addresses_for_tasks(0).keys())
        for index in range(1, num_hosts):
            common_intfs.intersection_update(
                driver.task_addresses_for_tasks(index).keys())
        if not common_intfs:
            raise Exception(
                'Unable to find a set of common task-to-task communication '
                'interfaces: %s'
                % [(index, driver.task_addresses_for_tasks(index))
                   for index in range(num_hosts)])
        return common_intfs
    finally:
        driver.shutdown()
