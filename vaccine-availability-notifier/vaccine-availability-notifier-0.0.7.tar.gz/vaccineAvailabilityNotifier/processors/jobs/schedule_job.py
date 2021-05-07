import time

import schedule

from vaccineAvailabilityNotifier.processors.jobs.process_job import ProcessJob


def execute_run():
    print("executing !!!")


class ScheduleJob:

    def __init__(self, sender_email_id, sender_email_password, pincodes, receiver_email, include_45):
        self.sender_email_id = sender_email_id
        self.sender_email_password = sender_email_password
        self.pincodes = pincodes
        self.receiver_email = receiver_email
        self.include_45 = include_45

    def schedule(self, time_in_seconds):
        schedule.every(time_in_seconds).seconds.do(execute_run)

        while True:
            ProcessJob(sender_email_id=self.sender_email_id,
                       sender_email_password=self.sender_email_password,
                       pincodes=self.pincodes, receiver_email=self.receiver_email,
                       include_45=self.include_45) \
                .process()
            print("running !!!")
            time.sleep(time_in_seconds)
