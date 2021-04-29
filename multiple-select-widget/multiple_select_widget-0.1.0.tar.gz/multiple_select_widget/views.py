import json
import operator
from functools import reduce

from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import View


class MultipleSelectWidgetView(View):
    """
    A basic view to handle filtering async for autocomplete.

    """

    # A list of the fields that will be queried on. They should follow
    # the format field__lookuptype.
    fields = ('pk__iexact', )
    # The model being filtered.
    model = None
    # The operator used to join on the queried fields. Not sure why anyone
    # would want to use something other than or, but customizability is good.
    default_operator = operator.or_
    obj_limit = None

    def get(self, request):
        """
        Determines the selected filter term, applies the filters to the
        base queryset, and finally returns a json object containing the
        matching results.

        params:
            :request: A request object. Expects the "filter" parameter.
        """
        filter_val = self.get_filter_val(request)

        base_queryset = self.get_queryset()
        results = self.get_results(filter_val, base_queryset)

        response = self.to_json(results)
        return HttpResponse(response, content_type="text/javascript")

    @staticmethod
    def get_filter_val(request):
        """
        Gets the requested filter value from the string.

        """
        return request.GET.get('filter', '')

    def get_queryset(self):
        """
        Get the base queryset that the filters will be applied to.

        """
        return self.model.objects.all()

    def get_results(self, filter_val, base_queryset):
        """
        Get a QueryDict of results matching the filter_val term.

        params:
            :filter_val: The term to be used in the queries.
            :base_queryset: The base set that will be further filtered using
                            filter_val.
        """
        if filter_val:
            q = [Q(**{field: filter_val}) for field in self.fields]
        if filter_val and q:
            new_base = base_queryset.filter(reduce(self.default_operator, q))
        else:
            # Return everything if no filter_val or fields are specified.
            # This allows for a very straightforward async request, but will
            # probably not behave as expected if no fields are specified.
            new_base = base_queryset

        if self.obj_limit:
            new_base = new_base[:self.obj_limit]

        return new_base

    @staticmethod
    def to_json(results):
        """
        Formats a list of db objects as a json object that is useable
        by the django-fsm-widget javascript.

        params:
            :results: An iterator of objects retrieved from the database.

        returns:
            A json object containing {object.pk: object_string_representation}
            for all of the objects in the results list. This is used to
            populate the available choices <select> with options of the format:
            <option value="object.pk">object_string_representation</option>
        """
        data = dict([(result.pk, str(result))for result in results])
        return json.dumps(data)
