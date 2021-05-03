# file sqltemplate/sqlcore.py

# Copyright (c) 2019-2021 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

import re
import copy

class SQLCore():
    """ The base class to all of the sqltemplate objects, which defines a method for copy and a number of methods to support templating.
    
    Args:
        template_values (dict,optional): If provided, sets the initial / default template values.
    """
    def __init__(self, template_values=None):
        self._template_values = {}
        if template_values:
            self.template_values = template_values

    @property
    def template_values(self):
        ''' The current template values for this sqltemplate entity. Template values are not applied until the sql for the entity is called, to allow for further replication or changing of the values. If the sqltemplate entity is copied or extended, the template_values are copied as default/initial parameters, but altering the template values after the copy is created will not propagate to the children.
        
        The setter fully replaces the template values dict by reference. To only add/change some values, use add_template_values '''
        return(self._template_values)

    @template_values.setter
    def template_values(self, template_values):
        self._template_values = template_values.copy() #do not set by reference


    def add_template_values(self, template_values):
        ''' Updates specific template values for this sqltemplate entity. This is additive - other template definitions that are not defined in the paramter will remain as they are.'''
        self.template_values.update(template_values)

    def apply_template(self, **template_values):
        """ This function returns the SQL for the current sqltemplate entity after applying all template values - including any template values that were predefined on the object along with any that are passed in to the function call.
        
        Args:
            template_values (dict, passed in a separate keyword arguments): Template values to include in the rendering of the SQL. These are not persistent and are not saved to the the object's template values.
        Returns:
            str: The SQL for the sqltemplate entity, after the internal template values and value parameters have been applied. 
        """
        return(self.apply_template_values(self.sql(), template_values))

    def extend_template(self, left_join=None, join_condition=None, **template_values):
        """ This function returns a new Query object with an expanded set of template values. Changing the new object will not affect the antecedent. This is used to create a new sqltemplate entity that has the template values defined, but that can be further composed in other sqltemplate contexts.
        
        Args:
            left_join (bool, optional): If not None, will set the left_join condition for the new, extended template entity. Only applicable for sqltemplate entities for which left_join is permitted.
            join_condition (list, optional): If provided, specifies the join condition for the new extended template. Only applicable for sqltemplate entitites for which join_condition is permitted.
            template_values (dict provided as additional keyword arguments): the default template values to set on the new object. 
        Returns:
            object: A copy of the current object that includes the new template_values.
        """
        copy_params = {}
        if left_join is not None:
            copy_params['left_join'] = left_join
        if join_condition is not None:
            copy_params['join_condition'] = join_condition
        newobj = self.copy(**copy_params)
        newobj.add_template_values(template_values)
        return(newobj)

    def copy(self, extend_template_values=None, **kwargs):
        newobj = copy.deepcopy(self)
        for arg, val in kwargs.items():
            if arg not in dir(newobj):
                raise Exception("Unknown parameter in copy: " + str(arg))
            setattr(newobj, arg, val)
        if extend_template_values:
            newobj.add_template_values(extend_template_values)
        return(newobj)


    @classmethod
    def apply_template_values(cls, sql, template_values):
        """ This function applies the template values to a given string (or array of strings) - note that this does not store the string internally. This is intended to be used as a mostly-private method.
        Args:
            sql (str|list): The sql string to apply the template values to.
            template_values (dict): The template values.
        Returns:
            str|list: The sql string(s) with the templates applied 
        """
        if not template_values:
            return(sql)

        if type(sql) in (list, tuple):
            resultlist = []
            for sql_string in sql:
                resultlist.append(cls.apply_template_values(sql_string, template_values))
            return(resultlist)

        # find all the possible keys
        direct_subs = re.findall(r'@\s?(\w+)\s?@', sql)
        # simple syntax '@key@': a single alphanumeric key, which should be defined in the template values to the per-instance value

        default_subs = re.findall(r"(@\s?(\w+)\s*\|\s*([^\@]+)\s?@)", sql)
        # default syntax '@key|0@', "@key|default@": if the key is not defined, use the default value.

        function_subs = re.findall(r'(@\s?(\S+)\s?:\s?(\w+)\s?@)', sql)
        # a functional sub is in the form @func:key@ where in which there is a function at the attribute template_function_{func} that will take in the sql, the clause, and the template value for the key

        for key in direct_subs:
            if key in template_values:
                sql = sql.replace('@' + key + '@', str(template_values[key]))

        for clause, key, default in default_subs:
            if key in template_values and template_values[key] is not None:
                sql = sql.replace(clause, str(template_values[key]))
            else:
                sql = sql.replace(clause, default)

        for clause, func, key in function_subs:
            if key in template_values:
                func = func.lower()

                # we allow custom template functions in subclasses by
                # creating a method call template_function_[func]
                method = getattr(cls, 'template_function_' + func)
                if not method:
                    raise Exception(f"template provided with function {func} (clause {clause} ) but that is not a known template function")
                sql = method(sql, clause, template_values[key])

        # out of date
        #for key, replacement in template_values.items():
        #    sql = sql.replace('@' + key + '@', str(replacement))
        return(sql)


    @classmethod
    def template_function_ne(klass, sql, clause, value):
        """ The definition of the ne template function. When the template is in the format '@ne:key@', the resultant SQL phrase will be '!= value' if value is singular or 'NOT IN (value[0], value[1], ...)' if value is multiple  """
        if type(value) is dict:
            negvalue = value.copy()
            negvalue['negate'] = True
            return(klass.template_function_eq(sql, clause, negvalue))
        else:
            return(klass.template_function_eq(sql, clause, {
                'negate': True,
                'value': value,
            }))

    @classmethod
    def template_function_eq(klass, sql, clause, value):
        """ The definition of the eq template function. When the template is in the format '@eq:key@', the resultant SQL phrase will be '= value' if value is singular or 'IN (value[0], value[1], ...)' if value is multiple  """

        negate = False
        if type(value) is dict:
            # additional parameters
            if 'negate' in value and value['negate']:
                negate = True
            value = value['value']

        if negate:
            IN = 'NOT IN'
            EQ = '!='
        else:
            IN = 'IN'
            EQ = '='

        if type(value) in (list, tuple,):
            if not len(value):
                raise Exception(f"Empty list not allowed as value for function '{func}' (clause '{clause}' )")
            if len(value) > 1:
                sql = sql.replace(clause, IN + " (" + ",".join([f"'{rep}'" if type(rep) is str else str(rep) for rep in value ]) + ")")
            else:
                if type(value[0]) is str:
                    sql = sql.replace(clause, EQ + " '" + value[0] + "'")
                else:
                    sql = sql.replace(clause, EQ + " " + str(value[0]))
        else:
            if type(value) is str:
                sql = sql.replace(clause, EQ + " '" + value + "'")
            else:
                sql = sql.replace(clause, EQ + " " + str(value))

        return(sql)

