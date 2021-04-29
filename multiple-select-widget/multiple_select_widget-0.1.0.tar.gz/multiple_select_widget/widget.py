# from django.contrib.admin.templatetags.admin_static import static
from django.forms import Media, SelectMultiple, ModelMultipleChoiceField
from django.forms.utils import flatatt
from django.templatetags.static import static


class MultipleSelectWidget(SelectMultiple):
    template_name = 'multiple_select_widget/multiple_select_widget.html'

    def __init__(self, verbose_name, url, use_async=False, attrs={},
                 choices=(), lazy=False, **kwargs):

        super(MultipleSelectWidget, self).__init__(attrs, choices, **kwargs)

        # If lazy is True the initial choices are not loaded with the template.
        self.lazy = lazy

        # The url used by the filter. Should route to a FormView that inherits
        # off of fsm.views.FSM.
        self.query_url = url

        # If use_async is True the initial choices are loaded after the <select>
        # fields used by the widget are finished loading. The initial choices
        # will be loaded using the query_url.
        self.use_async = use_async

        # The field name to be used for the widget.
        self.verbose_name = verbose_name

    @property
    def media(self):
        js = [static('js/multiple_select_widget.js')]
        css = {'all': (static('css/multiple_select_widget.css'), )}
        return Media(js=js, css=css)

    def get_context(self, name, value, attrs=None, choices=None):
        context = super().get_context(name, value, attrs)
        selected = value or []
        choices = choices or ()
        attrs = attrs or {}

        choices = dict(list(choices) + list(self.choices))
        selected_list = []

        # Remove the already-selected objects from the choices and put them
        # in the list of selected objects.
        for val in selected:
            if choices and val in choices:
                selection = choices.pop(val)
                selected_list.append((val, selection))

        final_attrs = {k:v for k, v in attrs.items() if k not in ['id', 'name']}

        choices_available = set(tuple(choices.items()))

        context['widget'].update({
            'use_async': self.use_async,
            'attrs': attrs,
            # If lazy-loading, don't pass in the choices.
            'choices': choices_available if not self.lazy else [],
            'final_attrs': flatatt(final_attrs),
            'name': name,
            'query_url': self.query_url,
            'selected': selected_list,
            'choices_count': len(choices_available),
            'selected_count': len(selected),
        })
        return context


class MSWModelMultipleChoiceField(ModelMultipleChoiceField):

    # Unpacks string of id's in a list
    # M2M Data is sent as a string compacted instead of multiple fields in form data
    # Workaround for this: The number of GET/POST parameters exceeded settings.DATA_UPLOAD_MAX_NUMBER_FIELDS
    def prepare_value(self, value):
        if (hasattr(value, '__iter__') and
                not isinstance(value, str) and
                not hasattr(value, '_meta')):
            prepare_value = super().prepare_value
            try:
                return [prepare_value(v) for v in value[0].split(',')]
            except (AttributeError, IndexError):
                # GET doesn't need unpacking
                return [prepare_value(v) for v in value]
        return super().prepare_value(value)
