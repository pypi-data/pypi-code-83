import click

from vaccineAvailabilityNotifier.processors.jobs.schedule_job import ScheduleJob


@click.command("schedule", help='schedule vaccine availability task')
@click.pass_context
@click.option('--include-45', '-i45', required=False, default=False, type=bool)
@click.option('--scheduler-time', '-st', required=False, default=5, type=int)
@click.option('--gmail-id', '-gid', required=True, default="bhasker.nandkishortest01@gmail.com", type=str)
@click.option('--gmail-password', '-gpass', required=False, default="System*#541", type=str)
@click.option('--receiver-email', '-re', required=False, default="bhasker.nandkishor@gmail.com", type=str)
@click.option('--pincodes', '-pcodes', nargs=0, required=True)
@click.argument('pincodes', nargs=-1)
def cmd(ctx, scheduler_time, gmail_id, gmail_password, pincodes, receiver_email, include_45):
    ScheduleJob(sender_email_id=gmail_id, sender_email_password=gmail_password,
                pincodes=pincodes, receiver_email=receiver_email, include_45=include_45) \
        .schedule(scheduler_time)
