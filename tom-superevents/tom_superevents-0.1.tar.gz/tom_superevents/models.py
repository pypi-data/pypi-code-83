from django.db import models


class Superevent(models.Model):
    """Represents a Superevent being followed-up upon by this TOM.

    A Superevent is distinguished from a Target in that it is localized to a region of the sky
    (vs. a specific RA,DEC). The potential Targets in the localization region must be identified,
    prioritized, and categorized (retired, of-interest, etc) for follow-up EM observations

    For the moment, this is rather GraceDB (GW) specific, but sh/could be generalized to work
    with gamma-ray burst and neutrino events.
    """

    class SupereventType(models.TextChoices):
        GRAVITATIONAL_WAVE = 'GW', 'Gravitational Wave'
        GAMMA_RAY_BURST = 'GRB', 'Gamma-ray Burst'
        NEUTRINO = 'NU', 'Neutrino'
        UNKNOWN = 'UNK', 'Unknown'

    superevent_type = models.CharField(
        max_length=3,
        choices=SupereventType.choices,
        default=SupereventType.GRAVITATIONAL_WAVE,
    )

    # TODO: ask Curtis/Rachel/Andy about generalized use cases.
    superevent_id = models.CharField(max_length=64)  # GraceDB superevent_id reference
    superevent_url = models.URLField()  # TODO: this should instead be constructed via superevent_id

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.superevent_id


class EventLocalization(models.Model):
    """Represents a region of the sky in which a superevent may have taken place.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
