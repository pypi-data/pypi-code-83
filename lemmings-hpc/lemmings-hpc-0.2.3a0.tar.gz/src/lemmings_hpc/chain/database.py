"""
Different usefull functions to interact with the database.yml file
"""
import os
import sys
import pkg_resources  # part of setuptools
from datetime import datetime
from pathlib import Path
from collections import namedtuple

import yaml
from prettytable import PrettyTable
import numpy as np

#from lemmings.chain.path_tool import PathTools
#from lemmings.chain.machine import convert
#from .machine import Machine  # circular import issue
#from lemmings.chain.machine import Machine

class Database:
    """Abstraction to interact with the database"""

    def __init__(self, db_path=None):
        if db_path is None:
            db_path = './database.yml'
        self.db_path = db_path
        self._initialise_db()

    @property
    def _database(self):
        """
        Get the informations from the database.yml file.*
        """

        with open(self.db_path) as fin:
            database = yaml.load(fin, Loader=yaml.FullLoader)
        return database

    @property
    def latest_chain_name(self):
        """Get the last chain name"""
        try:
            out = sorted(self._database, key=self.get_datetime)[-1]
        except IndexError:
            print("There is no chain in the Database 'database.yml'")
        return out

    @property
    def count(self):
        """
        *Get the loop number of a chain*
        """
        return int(len(self._database[self.latest_chain_name]))


    def _initialise_db(self):
        """
        *Create a Database if doesn't exist.*
        """
        if not Path(self.db_path).is_file():
            database = {}
            with open(self.db_path, 'w') as fout:
                yaml.dump(database, fout, sort_keys=False)


    def get_datetime(self, chain_name):
        """
        *Get the datetime of the first loop of a chain*
        """
        database = self._database
        time = database[chain_name][0]['datetime']
        datetime_obj = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

        return datetime_obj


    def initialise_new_chain(self, chain_name):
        """
        *Create a new chain dict{ } in the DB*
        """
        version = str(pkg_resources.require("lemmings_hpc")[0].version)
        database = self._database

        database[chain_name] = [{'lemmings_version': version,
                                 'datetime': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                 'safe_stop': False,
                                 'submit_path': './'}]
        with open(self.db_path, 'w') as fout:
            yaml.dump(database, fout, sort_keys=False)

    def initialise_new_loop(self):
        """Create a new loop in a chain"""
        database = self._database
        database[self.latest_chain_name].append({'datetime': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), #pylint: disable=line-too-long
                                                 'safe_stop': False,
                                                 'submit_path': './'})

        with open(self.db_path, 'w') as fout:
            yaml.dump(database, fout, sort_keys=False)


    def update_loop(self, key, value, index):
        """
        *Update the database of the current folder

        :param index: The loop number of the desired job
        :type index: int
        :param key: The name of the parameter to update or create
        :type key: str
        :param value: The value of the parameter
        :type value: all
        """
        database = self._database
        database[self.latest_chain_name][index-1][key] = value

        with open(self.db_path, 'w') as fout:
            yaml.dump(database, fout, sort_keys=False)


    def update_current_loop(self, key, value):
        """
        *Update the database of the current folder*

        :param key: The name of the parameter to update or create
        :type key: str
        :param value: The value of the parameter
        :type value: all
        """
        self.update_loop(key, value, self.count)

    def update_previous_loop(self, key, value):
        """
        *Update the database of the current folder*

        :param key: The name of the parameter to update or create
        :type key: str
        :param value: The value of the parameter
        :type value: all
        """
        self.update_loop(key, value, self.count-1)

    def update_first_loop(self, key, value):
        """
        *Update the database of the current folder*

        :param key: The name of the parameter to update or create
        :type key: str
        :param value: The value of the parameter
        :type value: all
        """
        self.update_loop(key, value, 1)


    def get_loop_val(self, key, index):
        """
        *Get the value of a parameter in a loop of a job.*

        :param key: The name of the parameter to update or create
        :type key: str
        """
        database = self._database
        return database[self.latest_chain_name][index - 1][key]


    def get_current_loop_val(self, key):
        """
        *Get the value of a parameter in a loop of a job.*

        :param key: The name of the parameter to update or create
        :type key: str
        """
        return self.get_loop_val(key, self.count)


    def get_first_loop_val(self, key):
        """
        *Get the value of a parameter in a loop of a job.*

        :param key: The name of the parameter to update or create
        :type key: str
        """
        return self.get_loop_val(key, 1)

    def get_previous_loop_val(self, key):
        """
        *Get the value of a parameter in a loop of a job.*

        :param key: The name of the parameter to update or create
        :type key: str
        """

        return self.get_loop_val(key, self.count-1)


    def get_chain_names(self):
        """
        *Get chain names from the database*
        """
        return list(self._database.keys())

    def set_progress_quantity(self, value):
        self.update_first_loop('progress_quantity', value)


    def get_current_status(self, keys = None):
        """
        Function returning the current status of the simulation.
        """
        # keys : is an option that could allow a future control of what to output
        #           but needs to be developed if eventually needed

        try:
            database = self._database # accesses the whole .yaml file
        except FileNotFoundError as excep:
            print("LemmingsError:", excep)
            return

        chain_name = self.latest_chain_name
        if chain_name is None:
            raise ValueError("No chain found. Check database.yml file in your current directory ...")

        #--Check first if the database is the main one of a parallel run---#
        parallel_run = False
        try:
            par_dict, = self.get_current_loop_val('parallel_runs')
            parallel_run = True
        except KeyError:
            pass

        if parallel_run:
            table = PrettyTable()
            table.field_names = ["Workflow number", "Status"]
            # match_val = {"start": "S", "hold": "H", "end": 'F'}
            # table.add_rows([[key, match_val[value]] if value in match_val
            #                     else [key, '?'] for key, value in par_dict.items()])

            symbol = {"start": "S", "hold": "H", "end": "F", "error": "E"}
            table.add_rows([(key, symbol.get(val, '?'))
                    for key, val in par_dict.items()])

            # keep for now in case we run with no match issue
            # table.field_names = ["Workflow number", "Status"]
            # for key, value in par_dict.items():
            #     val = "?"
            #     if value == "start":
            #         val = "S"
            #     elif value == "hold":
            #         val = "H"
            #     elif value == "end":
            #         val = "F"
            #     table.add_row([key,val])

            print("S: Submitted, F: Finished, H: Hold, E: Error")
            print(table)
            return


        print()
        print("Status for chain %s " % (chain_name))

        names_keys = keys
        if keys is None:
            # keys = ['solut_path', 'job_id', 'pjob_id', 'dtsum', 'end_cpu_time']
            keys = ['solut_path', 'condition_reached']
            progress_var = 'progress'
            # progress_title = 'progress'
            #progress_scale = 1
            try:
                progress_var = self.get_first_loop_val('progress_quantity')
               # progress_title = self.get_first_loop_val('progress_title')
                #progress_scale = self.get_first_loop_val('progress_scaling_factor')
            except KeyError:
                pass
            
            keys.append(progress_var)
            keys.extend(['end_cpu_time','job_id', 'pjob_id'])

            names_keys = ['Solution path', 'Job end status',
                            'progress', 'CPU time (h)',
                            'job ID', 'pjob ID']

            # if not progress_title == 'progress':
            #     names_keys = [key.replace('progress', progress_title) for key in names_keys]


        end_message = None

        match_cond_reached_keys = {'True': 'ended, finalized', 'False': 'ended, continue', 'None': 'ended, crashed'}
        table = PrettyTable()
        for ii, loop in enumerate(database[chain_name]):
            value_list = []

            # Separate handling of first loop situation
            if self.get_current_loop_val('loop_count') == 1:
                for key in keys:
                    if key in loop:
                        if key in ['solut_path']:
                            tmp_path = loop[key].split('/')[0]
                            if tmp_path == '.':
                                tmp_path = './'
                            value_list.append(tmp_path)
                        elif key in ['job_id', 'pjob_id']:
                            value_list.append(loop[key])
                        else:
                            value_list.append('Submitted')
                    else:
                        value_list.append('Submitted')
                value_list = [str(ii)] + value_list
                table.field_names = ["Loop"] + names_keys
                table.add_row(value_list)
                if loop["end_message"] is not None:
                    end_message = customise_end_message(self, ii, loop["end_message"])
                break

            if not 'solut_path' in loop and not 'job_id' in loop:
                # if 'job_id' in loop:
                #     continue
                if loop["end_message"] is not None:
                    end_message = customise_end_message(self, ii, loop["end_message"])
                break
            else:
                for key in keys:
                    if key in loop:
                        if key in [progress_var]:
                            tmp_key = np.round(loop[key],4)
                            value_list.append(tmp_key)
                        elif key in ['end_cpu_time']:
                            value_list.append(np.round(loop[key],3))
                        elif key in ['solut_path']:
                            tmp_path = loop[key].split('/')[0]
                            if tmp_path == '.' and tmp_path is not None:
                                tmp_path = './'
                            value_list.append(tmp_path)
                        elif key in ['condition_reached']:
                            tmp_key = loop[key]
                            value_list.append(match_cond_reached_keys[str(tmp_key)])
                        else:
                            value_list.append(loop[key])
                    else:
                        if 'condition_reached' not in loop:
                            value_list.append('Submitted')
                        elif key in [progress_var]:
                            value_list.append("NA")
                        elif 'solut_path' not in loop:
                            try:
                                tmp_path = self.get_first_loop_val('solut_path').split('/')[0]
                                if tmp_path == '.' and tmp_path is not None:
                                    tmp_path = './'
                                value_list.append(tmp_path)
                            except KeyError as excep:
                                continue
                        else:
                            value_list.append("NA")
                value_list = [str(ii)] + value_list
                table.field_names = ["Loop"] + names_keys
                table.add_row(value_list)

                if loop["end_message"] is not None:
                    end_message = customise_end_message(self, ii, loop["end_message"])

        print(table)
        if end_message is not None:
            print("Lemmings ended: " + end_message)
            print()


def customise_end_message(database, loop_num, end_msg):
    """ Function handling the end message output shown in 'lemmings status'

        Input:
            :database: database class object
            :loop_num: int, number of the loop calling this functionality
        Output:
            :end_message: str, ouput to be provided
    """

    if not isinstance(loop_num,int):
        loop_num = int(loop_num)

    if not loop_num == 0:
        end_message = "\n  Latest loop = %1d \n" % (loop_num - 1)
    else:
        end_message = "\n  Latest loop = %1d \n" % loop_num

    try:
        end_message += ["  Latest job and pjob IDs = "
                        + database.get_loop_val('job_id', (loop_num ))
                        + ' and ' + database.get_loop_val('pjob_id', (loop_num))
                        ][0]
    except KeyError:
       pass

    end_message += '\n  Final status: '+ end_msg
    return end_message
