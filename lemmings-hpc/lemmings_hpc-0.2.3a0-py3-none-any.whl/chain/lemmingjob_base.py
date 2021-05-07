from lemmings_hpc.chain.path_tool import PathTools
from lemmings_hpc.chain.database import Database

class LemmingJobBase():

    def __init__(self,
                 workflow,
                 machine,
                 loop_count,
                 status="start",
                 cpu_limit=None,
                 base_dir=None
                 ):


        self.pathtools = PathTools(base_dir)
        self.database = Database()
        self.workflow = workflow
        self.machine = machine
        self.status = status    #start, spawn_job, post_job, exit
        self.cpu_limit = cpu_limit
        self.loop_count = loop_count
        self.database.update_current_loop('loop_count',
                                          self.loop_count)
        self.end_message = None
        self.database.update_current_loop('end_message',
                                          self.end_message)


    """
    A lemming job follows always the same pattern.
    START > SPAWN JOB> POST JOB > SPAWN JOB > POST JOB > EXIT

    each step can be customized in the present class.
    e.g. you control the nb. of SPAWN JOB>POST JOB with the 'Check on end` function.


                 Prior to job  +---------+             Prepare run
                     +--------->SPAWN JOB+---------------------+
                     |         +------^--+                     |
                     |                |                      +-v------+
                   True               |                      |POST JOB|
    +-----+          |                |                      +--------+
    |START+--->Check on start         |                          v
    +-----+          |                +---------------False-Check on end
                   False            Prior to new iteration       +
                     |                                         True
                     |                                           |
                     |                                           |
                     |           +----+                          |
                     +---------->|EXIT|<-------------------------+
               Abort on start    +----+                After end job

    you can use the database if you need to store info from one job to the other.

    The following definition of methods allows a single lemmings run to be performed without any other user input
    except for the required .yml file information.

    """
    def prior_to_job(self):
        """
        Function that prepares the run when the user launches the Lemmings command.
        """

        pass

    def abort_on_start(self):
        """
        What lemmings does if the criterion is reached in the first loop.
        """

        pass

    def prepare_run(self):
        """
        Prepare the run before submission.
        """

        pass

    def prior_to_new_iteration(self):
        """
        Prepare the new loop specific actions if criterion is not reached.
        """

        pass

    def after_end_job(self):
        """
        Actions just before lemmings ends.
        """

        pass


    def check_on_start(self):
        """
        Verify if the condition is already satisfied before launching a lemmings chain.

        Function returns a boolean which starts the chain run. Default set to True.

        A minimum required action is to set the 'start_cpu_time' so that lemmings can check
        if the max cpu condition is reached.

        """

        self.database.update_current_loop('start_cpu_time', 0.)
        start_chain = True

        return start_chain


    def check_on_end(self):
        """
        Verifications after each job loop

         The function check_on_end needs to return a boolean (default True) with three options:
             - False: we continue lemmings
             - True: target reached, we stop lemmings (default setting)
             - None: crash, we stop lemmings

        Default verification by lemmings:
             - is the cpu condition (.yml file) reached?
         """

        condition_reached = True

        return condition_reached




class LemmingsStop(Exception):
    """ Definition of a class to allow exit of Lemmings safely upon exceptions
    """

    pass

