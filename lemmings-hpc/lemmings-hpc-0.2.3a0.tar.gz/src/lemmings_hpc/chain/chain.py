"""
This script execute the fundamentals functions of lemmings workflows.
"""
import sys
import os
import traceback
#import logging
#import yaml
from prettytable import PrettyTable

from lemmings_hpc.chain.database import Database
from lemmings_hpc.chain.lemmingjob_base import LemmingsStop

class Lemmings():
    """
    The mother class of Lemmings.
    """
    def __init__(self,
                 lemmings_job):
        """
        :param lemmings_job: An Object that contains all actions/
                             made in the different classical lemmings function:
                             --> function that check conditon(s)
                             --> function that do some actions before update status
                            For example, function "start_to_spawn_job()" can save a file, a fig ...
        """
        self.lemmings_job = lemmings_job
        self.database = Database()


    def run(self):
        """*Submit the chain of computations.*"""

        chain_name = self.lemmings_job.machine.job_name
        if not os.path.exists(chain_name):
            os.mkdir(chain_name)

        # logging.basicConfig(filename="lemmings.log", level=logging.INFO, format='%(message)s')

        # if self.lemmings_job.status == "start":
        #     logging.info("~~~~~~ START NEW Lemmings Chain ~~~~~~~\n")
        # else:
        #     logging.info("\n####### START NEW Lemmings loop #######")

        while self.lemmings_job.status != "exit":
            self.next()
        # else:
        #     print("Lemmings stopped: ", self.lemmings_job.end_message)
                # Could do print: Lemmings status = "started, aborted etc"
                # and in init of end_message = "Starting"
                # the other prints seem to be in log file instead ..
                # so do smth in the CLI? perhaps better to do so?


    def next(self):
        """
        Execute all necessary functions depending on its status
        There are 2 kind of function:
            - Functions that check some conditions
            - Functions that pass from a status to another
    ::

                     - - - > spawn_job < - - -
                    |             |             |
                    |             |             |
                  start             - - - - > post_job
            <check_condition>             <check_condition>
                    |                           |
                    |                           |
                    |                           |
                     - - - - - > Exit < - - - -
        """
        if self.lemmings_job.status == "start":
            try:
                # check_on_start() must return a boolean to start the lemmings job or not
                start_chain = self.lemmings_job.check_on_start()
                if start_chain:
                    self.lemmings_job.prior_to_job()
                    self._create_batch()
                    self.lemmings_job.status = "spawn_job"
                else:
                    self.lemmings_job.abort_on_start()
                    self.lemmings_job.status = "exit"
            except LemmingsStop as stop:
                #print(str(stop)) 
                ## really remove the above? I find this quite useful,
                ## if not output in terminal it will be in the slurm (or other) files
                self.lemmings_job.end_message = str(stop)
                self.database.update_current_loop('end_message',
                                                  self.lemmings_job.end_message)
                self.lemmings_job.status = "exit"
            except Exception as any_other_exception:
                self.lemmings_job.end_message = "Unexpected exception: "
                self.lemmings_job.end_message += str(any_other_exception)+"\n"
                self.lemmings_job.end_message += traceback.format_exc()
                traceback.print_exc()
                self.database.update_current_loop('end_message',
                                                  self.lemmings_job.end_message)
                #print(str(any_other_exception))
                self.lemmings_job.status = "exit"


        elif self.lemmings_job.status == "spawn_job":

            try:
                # Defined as one of the methods
                self.lemmings_job.prepare_run()
                safe_stop = self.database.get_previous_loop_val('safe_stop')
            except LemmingsStop as stop:
                self.lemmings_job.end_message = str(stop)
                self.database.update_current_loop('end_message',
                                                  self.lemmings_job.end_message)
                self.lemmings_job.status = "exit"
                safe_stop = True
            except Exception as any_other_exception:
                self.lemmings_job.end_message = "Unexpected exception: "
                self.lemmings_job.end_message += str(any_other_exception)+"\n"
                self.lemmings_job.end_message += traceback.format_exc()
                traceback.print_exc()
                self.database.update_current_loop('end_message',
                                                  self.lemmings_job.end_message)
                self.lemmings_job.status = "exit"
                safe_stop = True
            
            if safe_stop is False:
                submit_path = self.database.get_current_loop_val('submit_path')
                try:
                    job_id = self.lemmings_job.machine.submit(batch_name="batch_job",
                                                            submit_path=submit_path)
                except FileNotFoundError as excep:
                    print("LemmingsError:", excep)
                    sys.exit()
                try:
                    pjob_id = self.lemmings_job.machine.submit(batch_name="batch_pjob",
                                                            dependency=job_id,
                                                            submit_path="./")
                except FileNotFoundError as excep:
                    print("LemmingsError:", excep)
                    sys.exit()

                self.database.update_current_loop('job_id',
                                                job_id)
                self.database.update_current_loop('pjob_id',
                                                pjob_id)
            else:
                self.database.update_current_loop('safe_stop',
                                                True)
            self.lemmings_job.status = "exit"


        elif self.lemmings_job.status == "post_job":
            # A lemmings run is finished if
            #       1) the CPU limit is reached
            #       2) the target condition is reached (e.g. simulation end time)
            #       3) the simulation crashed for some reason
            # condition_reached can take 3 values:
            #       - False: we continue lemmings
            #       - True: target reached, we stop lemmings
            #       - None: crash, we stop lemmings

            # 1) check if cpu cost reached
            condition_reached = self._check_cpu_cost()

            # 2) check if target condition reached 3) or crash
            if not condition_reached:
                try:
                    condition_reached = self.lemmings_job.check_on_end()

                    if condition_reached is True or condition_reached is None:
                        self.database.update_previous_loop('condition_reached',
                                                        condition_reached)
                        self.database.update_current_loop('condition_reached',
                                                        condition_reached)
                        self.lemmings_job.after_end_job()
                        self.write_log_file()
                        self.lemmings_job.status = "exit"
                        if condition_reached is None:
                            self.lemmings_job.end_message = "Run crashed"
                        else:
                            self.lemmings_job.end_message = "Target condition reached"

                        self.database.update_current_loop('end_message',
                                    self.lemmings_job.end_message)


                    else:
                        self.database.update_previous_loop('condition_reached',
                                                    condition_reached)

                        self.lemmings_job.prior_to_new_iteration()
#                             output = self.lemmings_job.prior_to_new_iteration()
#                             if output is not None:
#                                 message = "Job_stopped by prior to new iteration method"
#                                 if len(output) > 1:
#                                     message += ": "+ output[1]
#                                 raise ValueError(message)
#                         except ValueError as excep:
#                             print(excep)
# #                        LemmingsStop as stop:
#  #                           print(str(stop))
#                             self.lemmings_job.status = "exit"
#                             pjob_id = self.database.get_previous_loop_val('pjob_id')
#                             self.lemmings_job.end_message = ["prior_to_new_iteration aborted the Lemmings Job."
#                                                             + " Check job id file " + str(pjob_id) + " for more info"][0]

#                             self.database.update_current_loop('end_message',
#                                                  self.lemmings_job.end_message)
#                             return
                        self._create_batch()
                        self.lemmings_job.status = "spawn_job"

                except LemmingsStop as stop:
                    self.lemmings_job.end_message = str(stop)
                    self.database.update_current_loop('end_message',
                                                    self.lemmings_job.end_message)
                    self.lemmings_job.status = "exit"
                except Exception as any_other_exception:
                    self.lemmings_job.end_message = "Unexpected exception: "
                    self.lemmings_job.end_message += str(any_other_exception)+"\n"
                    self.lemmings_job.end_message += traceback.format_exc()
                    traceback.print_exc()
                    self.database.update_current_loop('end_message',
                                                    self.lemmings_job.end_message)
                    self.lemmings_job.status = "exit"
            else:
                    # user condition is not reached but CPU limit is, so not update
                    # previous loop in present case
                    #self.database.update_previous_loop('condition_reached',
                    #                                    condition_reached)
                    self.database.update_current_loop('condition_reached',
                                                        condition_reached)
                    self.lemmings_job.after_end_job()
                    self.write_log_file()
                    self.lemmings_job.end_message = "Target CPU limit reached"
                    self.database.update_current_loop('end_message',
                                    self.lemmings_job.end_message)            
                    self.lemmings_job.status = "exit"    




    def _check_cpu_cost(self):
        """Check if the CPU limit is reached."""
        last_job_id = self.database.get_previous_loop_val('job_id')
        last_cpu_time = self.database.get_previous_loop_val('start_cpu_time')

        new_cpu_time = self.lemmings_job.machine.get_cpu_cost(last_job_id)
        total_cpu_time = last_cpu_time + new_cpu_time

        self.database.update_previous_loop('end_cpu_time',
                                           total_cpu_time)
        self.database.update_current_loop('start_cpu_time',
                                          total_cpu_time)


        if total_cpu_time > self.lemmings_job.cpu_limit:
            self.database.update_previous_loop('cpu_reached',
                                               True)
            self.lemmings_job.status = 'exit'
            self.lemmings_job.end_message = "CPU condition reached"

            self.database.update_current_loop('end_message',
                                    self.lemmings_job.end_message)

            return True
        return False


    def _create_batch(self, batch_j="./batch_job", batch_pj="./batch_pjob"):
        """
        Create the batch that will launch the job and postjob loop of lemmings.
        The construction is based on namedtuple that are unique for each machine.
        So the user, if not already done, have to set up those namedtuple for his machine(cluster).
        """

        # The user can take control of this step which can be done through the
        # expert_params object in the workflow's .yml file
        if hasattr(self.lemmings_job.machine.user, 'expert_params'):
            if 'user_batch' in self.lemmings_job.machine.user.expert_params:
                if self.lemmings_job.machine.user.expert_params['user_batch']:
                    return

        batch_job = self.lemmings_job.machine.job_template.batch
        batch_pjob = (self.lemmings_job.machine.pj_template.batch + '\n'
                      + "lemmings-hpc run "
                      + str(self.lemmings_job.workflow)
                      + " -s post_job" + '\n')

        with open(batch_j, 'w') as fout:
            fout.write(batch_job)
        with open(batch_pj, 'w') as fout:
            fout.write(batch_pjob)


    def write_log_file(self, usefull_keys=None):
        """write the log file"""
        chain_name = self.database.latest_chain_name
        database = self.database._database
        table = PrettyTable()

        if usefull_keys is None:
            usefull_keys = ['datetime', 'job_id', 'pjob_id', 'dtsum', 'end_cpu_time']

        if chain_name is None:
            raise ValueError("No chain found. Check database file in your current directory ...")
        else:
            log_msg = "Lemmings Version : " + str(database[chain_name][0]['lemmings_version']) + '\n\n'

            for i, loop in enumerate(database[chain_name]):
                value_list = []
                for key in usefull_keys:
                    if key in loop:
                        value_list.append(loop[key])
                    else:
                        value_list.append(None)
                value_list = [str(i)] + value_list
                table.field_names = ["Loop"] + usefull_keys
                table.add_row(value_list)
            log_msg += str(table)
            log_msg += "\n\n"

        if database[chain_name][-1]['safe_stop'] is True:
            log_msg += "Lemmings STOP because using 'safe stop' command\n"
        if 'run_crash' in database[chain_name][-2] and database[chain_name][-2]['run_crash'] is True:
            log_msg += "Your run CRASHED, see avbp.o file\n"
        elif 'condition_reached' in database[chain_name][-2] and database[chain_name][-2]['condition_reached']:
            if 'simu_end_time' in database[chain_name][0]:
                log_msg += ("Condition " + str(database[chain_name][0]['simu_end_time'])
                            + " [s] is     REACHED")

        with open(os.path.join(chain_name, chain_name + '.log'), 'w') as fout:
            fout.write(log_msg)


    # def write_log_file(self):
    #     """write the log file"""
    #     chain_name = self.database.latest_chain_name
    #     database = self.database._database

    #     usefull_keys = ['datetime', 'job_id', 'pjob_id', 'init_path', 'temporal_path', 'dtsum']
    #     columns_len = [20, 30]

    #     if chain_name is None:
    #         print("No chain found. Check database file in your current directory...")
    #     else:
    #         log_msg = ("\n#########################################\n"
    #                    + "         # Lemmings Version : "
    #                    + str(database[chain_name][0]['lemmings_version']) + " #         \n"
    #                    + "#########################################\n\n")


    #         for i, loop in enumerate(database[chain_name]):
    #             log_msg += "\n\n"
    #             log_msg += self.write_head(columns_len, i+1)

    #             for key in loop:
    #                 if key in usefull_keys:
    #                     key_blank_nb = self.adjust_column_size(key, size=20)
    #                     val_blank_nb = self.adjust_column_size(loop[key], size=30)
    #                     log_msg += ('|' + str(key) + key_blank_nb * " "
    #                                 + str(loop[key]) + val_blank_nb * " " + '|' + '\n')

    #                     log_msg += "├" + (sum(columns_len)) * " " + "┤"  + '\n'

    #             log_msg += "├" + (sum(columns_len)) * "-" + "┤"

    #         log_msg += "\n\n"
    #         log_msg += self.write_whole_chain_param(database, chain_name)

    #     with open(os.path.join(chain_name, chain_name + '.log'), 'w') as fout:
    #         fout.write(log_msg)


    # def adjust_column_size(self, key, size):

    #     word_len = len(str(key))
    #     return(size - word_len)

    # def write_head(self, columns_len, loop_nb):
    #     tot_size = sum(columns_len)
    #     log_msg =  "\n├" + (tot_size) * "-" + "┤" +'\n'

    #     log_msg += ('|' + (int(tot_size/2)-4)* " " + "LOOP N° " + str(loop_nb) + '|'
    #                 + self.adjust_column_size("LOOP N°", int(tot_size/2)) * " " + '\n')
    #     log_msg += "├" + tot_size * '-' + "┤" +'\n'
    #     return log_msg

    # def write_whole_chain_param(self, database, chain_name):

    #     log_msg = ("\n\nTotal physical time [s]   " + str(database[chain_name][-2]['dtsum']) + '\n'
    #                + "Total CPU cost [hours]    " + str(database[chain_name][-2]['end_cpu_time']) + '\n')


    #     if database[chain_name][-1]['safe_stop'] == True:
    #         log_msg += "Lemmings STOP because using 'safe stop' command "
    #     if 'run_crash' in database[chain_name][-2]:
    #         log_msg += "Your run CRASH, see avbp.o file"
    #     if 'condition_reached' in database[chain_name][-2]:
    #         log_msg += ("Condition " + str(database[chain_name][0]['simu_end_time'])
    #                     + " [s] is    REACHED")

    #     return log_msg
