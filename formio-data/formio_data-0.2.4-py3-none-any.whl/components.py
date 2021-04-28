# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import json
import uuid

from collections import OrderedDict
from datetime import datetime

from formiodata.utils import base64_encode_url, decode_resource_template, fetch_dict_get_value


class Component:

    def __init__(self, raw, builder, **kwargs):
        self.raw = raw
        self.builder = builder

        self._parent = None
        self._component_owner = None
        # components can also be seen as children
        self.components = OrderedDict()

        # XXX uuid to ensure (hope this won't break anything)
        self.id = self.raw.get('id', str(uuid.uuid4()))

        # submission {key: value, ...}
        self.form = {}

        # i18n (language, translations)
        self.language = kwargs.get('language', 'en')
        self.i18n = kwargs.get('i18n', {})
        self.resources = kwargs.get('resources', {})
        if self.resources and isinstance(self.resources, str):
            self.resources = json.loads(self.resources)
        self.html_component = ""
        self.defaultValue = self.raw.get('defaultValue')

    def load_value(self, data):
        if self.input and data:
            if isinstance(data, dict) and data.get(self.key):
                self.value = data[self.key]
                self.raw_value = data[self.key]
            else:
                self.value = data
                self.raw_value = data

    def load(self, component_owner, parent=None, data=None):
        self.component_owner = component_owner

        self.load_value(data)

        if parent:
            self.parent = parent

        self.builder.component_ids[self.id] = self

        # (Input) nested components (e.g. datagrid, editgrid)
        for component in self.raw.get('components', []):
            # Only determine and load class if component type.
            if 'type' in component:
                component_obj = self.builder.get_component_object(component)
                component_obj.load(self.child_component_owner, parent=self, data=data)

        # (Layout) nested components (e.g. columns, panels)
        for k, vals in self.raw.copy().items():
            if isinstance(vals, list):
                for v in vals:
                    if 'components' in v:
                        for v_component in v['components']:
                            v_component_obj = self.builder.get_component_object(v_component)
                            if v_component_obj.id not in self.builder.component_ids:
                                v_component_obj.load(self.child_component_owner, parent=self, data=data)
                    elif isinstance(v, list):
                        # table component etc. which holds even deeper lists with components
                        for list_v in v:
                            if 'components' in list_v:
                                for list_v_component in list_v.get('components'):
                                    if list_v_component.get('type'):
                                        list_v_component_obj = self.builder.get_component_object(list_v_component)
                                        if list_v_component_obj.id not in self.builder.component_ids:
                                            list_v_component_obj.load(self.child_component_owner, parent=self, data=data)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id=False):
        if not id:
            id = str(uuid.uuid4())
        self._id = id

    @property
    def key(self):
        return self.raw.get('key')

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if parent:
            self._parent = parent
            self._parent.components[self.key] = self

    @property
    def is_form_component(self):
        return bool(self.input)

    @property
    def component_owner(self):
        """The component's "owner".  This is usually the Builder class which
        created it.  But if this component is inside a datagrid
        component which may clone the form element, then the datagrid
        is the owner.  Each component adds itself to the `form_components`
        property its owner.
        """
        return self._component_owner

    @component_owner.setter
    def component_owner(self, component_owner):
        self._component_owner = component_owner
        if self.is_form_component:
            self._component_owner.form_components[self.key] = self

    @property
    def child_component_owner(self):
        """The owner object for child components, to use in the recursion"""
        return self.component_owner

    @property
    def type(self):
        return self.raw.get('type')

    @property
    def input(self):
        return self.raw.get('input')

    @property
    def valdidate(self):
        return self.raw.get('validate')

    @property
    def required(self):
        return self.raw.get('validate').get('required')

    @property
    def properties(self):
        return self.raw.get('properties')

    @property
    def label(self):
        label = self.raw.get('label')
        if self.i18n.get(self.language):
            return self.i18n[self.language].get(label, label)
        else:
            return label

    @label.setter
    def label(self, value):
        if self.raw.get('label'):
            self.raw['label'] = value

    @property
    def value(self):
        return self.form.get('value')

    @value.setter
    def value(self, value):
        self.form['value'] = self._encode_value(value)

    @property
    def raw_value(self):
        return self.form['raw_value']

    @raw_value.setter
    def raw_value(self, value):
        self.form['raw_value'] = value

    @property
    def hidden(self):
        return self.raw.get('hidden')

    def _encode_value(self, value):
        return value

    def render(self):
        self.html_component = '<p>%s</p>' % self.form.get('value')


# Basic

class textfieldComponent(Component):
    pass


class textareaComponent(Component):
    pass


class numberComponent(Component):
    pass


class passwordComponent(Component):
    pass


class checkboxComponent(Component):
    pass


class selectboxesComponent(Component):

    @property
    def values_labels(self):
        comp = self.component_owner.form_components.get(self.key)
        builder_values = comp.raw.get('values')
        values_labels = {}
        for b_val in builder_values:
            if self.value and b_val.get('value'):
                if self.i18n.get(self.language):
                    label = self.i18n[self.language].get(b_val['label'], b_val['label'])
                else:
                    label = b_val['label']
                val = {'key': b_val['value'], 'label': label, 'value': self.value.get(b_val['value'])}
                values_labels[b_val['value']] = val
        return values_labels


class selectComponent(Component):

    @property
    def multiple(self):
        return self.raw.get('multiple')

    @property
    def value_label(self):
        comp = self.component_owner.form_components.get(self.key)
        values = comp.raw.get('data') and comp.raw['data'].get('values')
        for val in values:
            if val['value'] == self.value:
                label = val['label']
                if self.i18n.get(self.language):
                    return self.i18n[self.language].get(label, label)
                else:
                    return label
        else:
            return False

    @property
    def value_labels(self):
        comp = self.component_owner.form_components.get(self.key)
        values = comp.raw.get('data') and comp.raw['data'].get('values')
        value_labels = []
        for val in values:
            if val['value'] in self.value:
                if self.i18n.get(self.language):
                    value_labels.append(self.i18n[self.language].get(val['label'], val['label']))
                else:
                    value_labels.append(val['label'])
        return value_labels


class radioComponent(Component):

    @property
    def values_labels(self):
        comp = self.component_owner.form_components.get(self.key)
        builder_values = comp.raw.get('values')
        values_labels = {}

        for b_val in builder_values:
            if self.i18n.get(self.language):
                label = self.i18n[self.language].get(b_val['label'], b_val['label'])
            else:
                label = b_val['label']
            val = {'key': b_val['value'], 'label': label, 'value': b_val['value'] == self.value}
            values_labels[b_val['value']] = val
        return values_labels

    @property
    def value_label(self):
        comp = self.component_owner.form_components.get(self.key)
        builder_values = comp.raw.get('values')
        value_label = {}

        for b_val in builder_values:
            if b_val['value'] == self.value:
                if self.i18n.get(self.language):
                    return self.i18n[self.language].get(b_val['label'], b_val['label'])
                else:
                    return b_val['label']
        else:
            return False


class buttonComponent(Component):

    @property
    def is_form_component(self):
        return False

    def load_value(self, data):
        # just bypass this
        pass


# Advanced

class emailComponent(Component):
    pass


class urlComponent(Component):
    pass


class phoneNumberComponent(Component):
    pass


# TODO: tags, address


class datetimeComponent(Component):

    def _format_mappings(self):
        """
        Dictionary of mappings between Formio Datetime component
        (key) to Python format (value).

        Formio uses the format codes refererend in:
        https://github.com/angular-ui/bootstrap/tree/master/src/dateparser/docs#uibdateparsers-format-codes
        """
        return {
            'year': {'yyyy': '%Y', 'yy': '%y', 'y': '%y'},
            'month': {'MMMM': '%B', 'MMM': '%b', 'MM': '%m', 'M': '%-m'},
            'day': {'dd': '%d', 'd': '%-d'},
            'hour': {'HH': '%HH', 'H': '%-H', 'hh': '%I', 'h': '%-I'},
            'minute': {'mm': '%M', 'm': '%-M'},
            'second': {'ss': '%S', 's': '%-S'},
            'am_pm': {'a': '%p'}
        }

    def _fromisoformat(self, value):
        # Backport of Python 3.7 datetime.fromisoformat
        if hasattr(datetime, 'fromisoformat'):
            # Python >= 3.7
            return datetime.fromisoformat(value)
        else:
            # Python < 3.7
            # replaces the fromisoformat, not available in Python < 3.7
            #
            # XXX following:
            # - Raises: '2021-02-25T00:00:00+01:00' does not match format '%Y-%m-%dT%H:%M%z'
            # - Due to %z not obtaing the colon in '+1:00' (tz offset)
            # - More info: https://stackoverflow.com/questions/54268458/datetime-strptime-issue-with-a-timezone-offset-with-colons
            # fmt_str =  r"%Y-%m-%dT%H:%M:%S%z"
            # return datetime.strptime(value, fmt_str)
            #
            # REQUIREMENT (TODO document, setup dependency or try/except raise exception)
            # - pip install dateutil
            # - https://dateutil.readthedocs.io/
            from dateutil.parser import parse
            return parse(value)

    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, value):
        """ Inherit property setter the right way, URLs:
        - https://gist.github.com/Susensio/979259559e2bebcd0273f1a95d7c1e79
        - https://stackoverflow.com/questions/35290540/understanding-property-decorator-and-inheritance
        """
        # TODO: to improve these transformations (mappings and loops)

        if not value:
            return value

        component = self.component_owner.form_components.get(self.key)
        dt = self._fromisoformat(value)
        py_dt_format = formio_dt_format = component.raw.get('format')
        mapping = self._format_mappings()

        # year
        done = False
        for formio, py in mapping['year'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        # month
        done = False
        for formio, py in mapping['month'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        #day
        done = False
        for formio, py in mapping['day'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        # hour
        done = False
        for formio, py in mapping['hour'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        # minute
        done = False
        for formio, py in mapping['minute'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        # second
        done = False
        for formio, py in mapping['second'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        # 12 hours AM/PM
        done = False
        for formio, py in mapping['am_pm'].items():
            if not done and formio in formio_dt_format:
                py_dt_format = py_dt_format.replace(formio, py)
                done = True

        val = dt.strftime(py_dt_format)
        super(self.__class__, self.__class__).value.fset(self, val)

    def to_datetime(self):
        if not self.raw_value:
            return None
        dt = self._fromisoformat(self.raw_value)
        return dt

    def to_date(self):
        if not self.raw_value:
            return None
        return self.to_datetime().date()


class timeComponent(Component):
    pass


class currencyComponent(Component):
    pass


class surveyComponent(Component):
    pass


class signatureComponent(Component):
    pass


# Layout components

class htmlelementComponent(Component):
    pass


class contentComponent(Component):
    pass


class layoutComponentBase(Component):
    pass


class columnsComponent(layoutComponentBase):

    @property
    def rows(self):
        rows = []

        row = []
        col_data = {'column': None, 'components': []}
        total_width = 0

        for col in self.raw['columns']:
            components = []

            for col_comp in col['components']:
                for key, comp in self.components.items():
                    if col_comp['id'] == comp.id:
                        components.append(comp)

            if col['width'] >= 12:
                # add previous (loop) row
                if row:
                    rows.append(row)

                # init new row and add to rows
                row = [{'column': col, 'components': components}]
                rows.append(row)

                # init next loop (new row and total_width)
                row = []
                total_width = 0
            elif total_width >= 12:
                # add previous (loop) row
                rows.append(row)
                row = []
                # init new row for next loop
                col_data = {'column': col, 'components': components}
                row.append(col_data)
                total_width = col['width']
            else:
                if not row:
                    row = [{'column': col, 'components': components}]
                else:
                    col_data = {'column': col, 'components': components}
                    row.append(col_data)
                total_width += col['width']
        if row:
            # add last generated row
            rows.append(row)
        return rows


class fieldsetComponent(layoutComponentBase):
    pass


class panelComponent(layoutComponentBase):

    @property
    def title(self):
        title = self.raw.get('title')
        if not title:
            title = self.raw.get('label')

        if self.i18n.get(self.language):
            return self.i18n[self.language].get(title, title)
        else:
            return title


class tableComponent(layoutComponentBase):

    @property
    def rows(self):
        rows = []
        for row in self.raw['rows']:
            row_components = []

            for cols in row:
                for col_comp in cols['components']:
                    for key, comp in self.components.items():
                        if col_comp['id'] == comp.id:
                            row_components.append(comp)
            rows.append(row_components)
        return rows


class tabsComponent(layoutComponentBase):

    @property
    def tabs(self):
        tabs = []
        for tab in self.raw['components']:
            add_tab = {
                'tab': tab,
                'components': []
            }
            for comp in tab['components']:
                for key, comp in self.components.items():
                    if comp['key'] == comp.key:
                        add_tab['components'].append(comp[1])
            tabs.append(add_tab)
        return tabs


# Data components

class datagridComponent(Component):

    def __init__(self, raw, builder, **kwargs):
        # TODO when adding other data/grid components, create new
        # dataComponent class these can inherit from.
        self.form_components = {}
        self.rows = []
        super().__init__(raw, builder, **kwargs)
        self.form = {'value': []}

    def load_value(self, data):
        if data:
            self._load_rows(data)

        if self.input and data:
            if isinstance(data, dict) and data.get(self.key):
                self.value = data[self.key]
            else:
                self.value = data

    def _load_rows(self, data):
        rows = []

        for row in self.value:
            # EXAMPLE row:
            # [{'email': 'personal@example.com'}, {'typeOfEmail': 'personal'}]

            new_row = []
            slots_todo = []
            slots_done = []

            for slot in row:
                # EXAMPLE slot:
                # {'email': 'personal@example.com'}
                for key, val in slot.items():
                    # EXAMPLE:
                    # key => 'email'
                    # val => 'personal@example.com'
                    for key, comp in self.components.items():
                        if key == comp.key:
                            raw = comp.raw
                            new_slot = self.builder.get_component_object(raw)
                            new_slot.value = val
                            new_row.append(new_slot)
                            slots_done.append(key)
                    if key not in slots_done:
                        slots_todo.append(slot)
            if slots_todo:
                for key, comp in self.components.items():
                    if hasattr(comp, 'propagate_children'):
                        new_row.append(comp.propagate_children(slots_todo))
            if new_row:
                rows.append(new_row)
        self.rows = rows

    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, value=[]):
        if not isinstance(value, list):
            value = []
        self.rows = []
        for row in value:
            add_row = {}
            for key, val in row.items():
                component = self.form_components[key]
                component_object = self.builder.get_component_object(component.raw)
                component_object.component_owner = self
                component_object.value = val
                component_object.raw_value = val
                add_row[key] = component_object
            self.rows.append(add_row)
        super(self.__class__, self.__class__).value.fset(self, self.rows)

    @property
    def labels(self):
        labels = OrderedDict()
        for comp in self.raw['components']:
            if self.i18n.get(self.language):
                label = self.i18n[self.language].get(comp['label'], comp['label'])
            else:
                label = comp['label']
            labels[comp['key']] = label
        return labels

    @property
    def is_form_component(self):
        # NOTE: A datagrid is not _really_ a form component, but it
        # has a key in the JSON for loading the form, so it acts as
        # such, and it will create an entry in the "form_components"
        # property of its owner.
        return True


    @property
    def child_component_owner(self):
        return self


# Premium components

class fileComponent(Component):

    def __init__(self, raw, builder, **kwargs):
        super().__init__(raw, builder, **kwargs)

    @property
    def storage(self):
        return self.raw.get('storage')

    @property
    def url(self):
        return self.raw.get('url')

    @property
    def base64(self):
        if self.storage == 'url':
            res = ''
            for val in self.form.get('value'):
                name = val.get('name')
                url = val.get('url')
                res += base64_encode_url(url)
            return res
        elif self.storage == 'base64':
            return super().value

    # @value.setter
    # def value(self, value):
    #     """ Inherit property setter the right way, URLs:
    #     - https://gist.github.com/Susensio/979259559e2bebcd0273f1a95d7c1e79
    #     - https://stackoverflow.com/questions/35290540/understanding-property-decorator-and-inheritance
    #     """
    #     super(self.__class__, self.__class__).value.fset(self, value)


class resourceComponent(Component):

    def __init__(self, raw, builder, **kwargs):
        super().__init__(raw, builder, **kwargs)
        self.item_data = {}
        self.template_label_keys = decode_resource_template(self.raw.get('template'))
        self.compute_resources()

    def compute_resources(self):
        if self.resources:
            resource_id = self.raw.get('resource')
            if resource_id and not resource_id == "" and resource_id in self.resources:
                resource_list = self.resources[resource_id]
                self.raw['data'] = {"values": []}
                for item in resource_list:
                    label = fetch_dict_get_value(item, self.template_label_keys[:])
                    self.raw['data']['values'].append({
                        "label": label,
                        "value": item['_id']['$oid']
                    })

    @property
    def value_label(self):
        comp = self.component_owner.form_components.get(self.key)
        values = comp.raw.get('data') and comp.raw['data'].get('values')
        for val in values:
            if val['value'] == self.value:
                label = val['label']
                if self.i18n.get(self.language):
                    return self.i18n[self.language].get(label, label)
                else:
                    return label
        else:
            return False

    @property
    def value_labels(self):
        comp = self.component_owner.form_components.get(self.key)
        values = comp.raw.get('data') and comp.raw['data'].get('values')
        value_labels = []
        for val in values:
            if val['value'] in self.value:
                if self.i18n.get(self.language):
                    value_labels.append(self.i18n[self.language].get(val['label'], val['label']))
                else:
                    value_labels.append(val['label'])
        return value_labels

    @property
    def data(self):
        return self.raw.get('data')

    @property
    def values(self):
        return self.raw.get('data').get('values')
