from huscy.bookings.services import book_timeslot
from huscy.pseudonyms.services import get_or_create_pseudonym
from huscy.participations.models import Attendance, Participation


def create_participation(subject_group, subject, timeslots=[]):
    pseudonym = get_or_create_pseudonym(subject, 'participations.participation',
                                        object_id=subject_group.id).code
    if not timeslots:
        participation = _create_declined_participation(pseudonym, subject_group)
    else:
        participation = _create_pending_participation(pseudonym, subject_group, subject, timeslots)

    # TODO: update participation request to status invited

    return participation


def _create_declined_participation(pseudonym, subject_group):
    return Participation.objects.create(pseudonym=pseudonym, subject_group=subject_group)


def _create_pending_participation(pseudonym, subject_group, subject, timeslots):
    participation = Participation.objects.create(pseudonym=pseudonym, subject_group=subject_group,
                                                 status=Participation.STATUS.get_value('pending'))
    for timeslot in timeslots:
        timeslot = book_timeslot(timeslot, subject)
        Attendance.objects.create(participation=participation, booking=timeslot.booking_set.get(),
                                  start=timeslot.start, end=timeslot.end)
    return participation


def get_participations(experiment, subject_group=None):
    participations = Participation.objects.filter(subject_group__experiment=experiment)
    if subject_group:
        participations = participations.filter(subject_group=subject_group)
    return participations
