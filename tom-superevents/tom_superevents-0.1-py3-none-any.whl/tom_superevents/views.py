from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework import permissions

from tom_superevents.superevent_clients.gravitational_wave import GravitationalWaveClient
from .models import Superevent, EventLocalization
from .serializers import SupereventSerializer, EventLocalizationSerializer


class SupereventListView(ListView):
    model = Superevent
    template_name = 'tom_superevents/index.html'


class SupereventDetailView(DetailView):
    model = Superevent
    template_name = 'tom_superevents/detail.html'

    # TODO: consider combining these dictionaries
    template_mapping = {
        Superevent.SupereventType.GRAVITATIONAL_WAVE: 'tom_superevents/superevent_detail/gravitational_wave.html',
        Superevent.SupereventType.GAMMA_RAY_BURST: 'tom_superevents/superevent_detail/gamma_ray_burst.html',
        Superevent.SupereventType.NEUTRINO: 'tom_superevents/superevent_detail/neutrino.html',
    }
    client_mapping = {
        Superevent.SupereventType.GRAVITATIONAL_WAVE: GravitationalWaveClient,
        Superevent.SupereventType.GAMMA_RAY_BURST: None,
        Superevent.SupereventType.NEUTRINO: None,
        Superevent.SupereventType.UNKNOWN: None,
    }

    def get_template_names(self):
        obj = self.get_object()
        return [self.template_mapping[obj.superevent_type]]

    # TODO: error handling
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        superevent_client = GravitationalWaveClient()
        context['superevent_data'] = superevent_client.get_superevent_data(self.object.superevent_id)
        context.update(superevent_client.get_additional_context_data(self.object.superevent_id))
        return context


# Django Rest Framework Views


class SupereventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Superevents to be viewed or edited.
    """
    queryset = Superevent.objects.all()
    serializer_class = SupereventSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventLocalizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EventLocalizations to be viewed or edited.
    """
    queryset = EventLocalization.objects.all()
    serializer_class = EventLocalizationSerializer
    permission_classes = [permissions.IsAuthenticated]
