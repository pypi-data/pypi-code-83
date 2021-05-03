# file sqltemplate/clause.py

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
from .sqlcore import SQLCore
from . import flatten

#
# List the functions that are ignored if AUTOGROUP is true. It is okay to support proprietary functions so long as they do not conflict with ANSI/standardized functions that are named the same but not aggregate.
#
aggregate_functions = [
    'APPROX_COUNT_DISTINCT',
    'AVG',
    'COLLECT',
    'CORR\w+',
    'COUNT',
    'COVAR_POP',
    'COVAR_SAMP',
    'CUME_DIST',
    'DENSE_RANK',
    'FIRST',
    'GROUP_ID',
    'GROUPING',
    'GROUPING_ID',
    'LAST',
    'LISTAGG',
    'MAX',
    'MEDIAN',
    'MIN',
    'PERCENT_RANK',
    'PERCENTILE_CONT',
    'PERCENTILE_DISC',
    'RANK',
    'REGR\w+',
    'STATS_BINOMIAL_TEST',
    'STATS_CROSSTAB',
    'STATS_F_TEST',
    'STATS_KS_TEST',
    'STATS_MODE',
    'STATS_MW_TEST',
    'STATS_ONE_WAY_ANOVA',
    'STATS_T_TEST\w+',
    'STATS_WSR_TEST',
    'STDDEV',
    'STDDEV_POP',
    'STDDEV_SAMP',
    'SUM',
    'SYS_OP_ZONE_ID',
    'SYS_XMLAGG',
    'VAR_POP',
    'VAR_SAMP',
    'VARIANCE',
    'XMLAGG',
]

# precompile some complex regexps
aggfuncre = re.compile(r'('+'|'.join(aggregate_functions)+r')\s*\(', re.I)
selectas = re.compile(r'\s+AS\s+\w+\s*(,|$)', re.I)

def make_group_from_select(select):
    """ Makes a group by clause given the select clause provided. It does this by ignoring aggregate clauses and removing any aliasing. This is intended to having to avoid the repetition of non-aggregate functions in the group by clause.

    Args:
        select (str|list|sqltemplate.Clause): the select clause to generate the group by from.
    Return:
        list|None: A list of group-by phrases analogous to the provided select phrase, or None if the select phrase does not include any fields that can be grouped.  
    """
    tselect = type(select)
    if tselect is str:
        if aggfuncre.search(select):
            # aggregate functions are not included in group
            return
        #strip out any "AS" statements, but make sure to leave the
        # commas in case there are multiple fields nested in the same
        # string.
        return([selectas.sub(lambda x: x.group(1), select)])
    elif tselect in (list, tuple):
        where_clause = []
        for val in select:
            where_statement = make_group_from_select(val)
            if where_statement:
                where_clause.extend(where_statement)
        return(where_clause)
    elif isinstance(select, Clause):
        return(make_group_from_select(select.values))
    else:
        raise Exception("Cannot make a group function from unknown type " + str(tselect))


class Clause(SQLCore):
    """ A clause object is a combination of atomic phrases. When generating SQL, phrases within a Clause are combined with a separator and potentially other processing. Note that the full set of phrases are actually composed of two parts: the phrase and the suffix. The suffix allows you to define composable objects that allow future copies to add phrases between the regular phrases nad the suffix. For example, you set a SELECT Clause that predefines the initial columns and then sets some unimportant columns using the suffix.  As the object is copied and additional phrases are appended, they precede the unimportant columns.

    Args:
        phrases(args): A list of phrases that comprise the clause. Subclasses can modify it, but a phrase often can be a string, another Clause, or a Query.
        template_values (dict, optional): the default/initial mapping of template terms -> template values for this clause and all contained phrases.
        suffix (list|clause, optional): a phrase or set of phrases that is appended to the end of the list. 
    """
    default_separator=",\n\t"

    def __init__(self, *phrases, template_values=None, suffix=None):
        super().__init__(template_values=template_values)

        self._values = []
        self.extend(phrases)
        if suffix:
            self._suffix = suffix
        else:
            self._suffix = []
        self._separator = self.default_separator

    @property
    def separator(self):
        """ str: the separator for the phrases of this clause. """
        return(self._separator)

    @separator.setter
    def separator(self, new_sep):
        self._separator = new_sep


    @property
    def n(self):
        """ The current number of distinct phrases in the clause (Note that this is not recursive).

        Note: This won't necessarily be a conceptually useful count because a single phrase can be another clause with multiple phrases. """
        return(len(self.values))

    @property
    def values(self):
        """ Values by itself returns a shallow copy of the list of all phrases (including suffix phrases), so manipulation doesn't inadvertently modify the list or order. However, if the phrase is itself an object (like a Query or another Clause), modifications to it will be real. To modify the list, use one of the many array-ish functions."""
        result = []
        for val in self._values:
            result.append(val)
        for val in self._suffix:
            result.append(val)
        return (result)

    @property
    def phrases(self):
        """ Accessor to the main phrase list - note that in the present implementation this provides a reference to the actual list, so modification will change the values therein. """
        return(self._values)

    @property
    def suffix(self):
        """ Accessor to the suffix list - note that in the present implementation this provides a reference to the actual list, so modification will change the values therein. """
        return(self._suffix)

    def copy(self, extend=None, **kwargs):
        """ Deep copy the clause and create copies of any phrases that are objects, so that changes to the the copy or any of its components do not change the upstream source entities.

        Args:
            extend(list, optional): A list of additional phrases to append to the copied object.
            kwargs (additional keyword arguments): Pass-through parameters for the call to the superclass (SQLCore) copy
        """
        new_version = super().copy(**kwargs)
        if extend:
            new_version.extend(extend)
        return(new_version)

    def remove(self, value):
        """ Removes a specific value (case insensitive) from the list, regardless of the index. At present, this will recurse through lists but not through subsidiary clauses or queries. """
        self.remove_from_array(self._values, value)

    def replace(self, to_replace, replace_with, reflags=None, case_sensitive=None):
        """ Replaces one string with another, recursively. This will go through all of the phases within the clause and do a string replace. No copies are generated, and so calling replace on a component used elsewhere will apply those changes to all downstream elements.
        Note:
            This recursively will replace strings or call replace on:
                A. the phrases and suffix phrases of this object, including recursive calls to any other Clauses or Queries in the phrase list.
                B. Any template or template values
        Args:
            to_replace (str): The string to match on, using the regular expression lexicon of re.
            replace_with (str): The string to replace with, using the regular expression lexicon of re.
            reflags: Any flags to apply to the regular expression.
            case_sensitive (bool): Whether the match should be case sensitive. If False, the re.I flag is set. The re.I flag will be combined with reflags if both are defined in the function call; however, if reflags is defined and case_sensitive is not, no default case_sensitive argument is processed. By default, if reflags is not provided, this is False and the replace will operate as case-insensitve.
            """

        if reflags is None:
            if not case_sensitive:
                reflags = re.I
            else:
                reflags = 0
        elif case_sensitive is not None:
            if not case_sensitive:
                reflags |= re.I

        rex = re.compile(to_replace, reflags)

        def recursive_replace(elem):
            if type(elem) in (list, tuple):
                return([recursive_replace(subelem) for subelem in elem])
            return(rex.sub(replace_with, elem))

        # go through all of the values and replace them
        for i, value in enumerate(self.values):
            if isinstance(value, Clause) or isinstance(value, Query):
                value.replace(to_replace, replace_with)
            elif i < len(self._values):
                self._values[i] = recursive_replace(value)
            else:
                self._suffix[i - len(self._values)] = recursive_replace(value)

        #also go through all of the template rules and replace anything in the values
        for template in self.template_values:
            if type(self.template_values[template]) is str:
                self.template_values[template] = self.template_values[template].replace(to_replace, replace_with)

    def sql(self, sep=None, template_values=None, extend=None):
        """ return a string of the sql for this clause.

        Args:
            sep (str): A separator to override the default.
            template_values (dict): A mapping of additional template values to apply to the generation of this sql statement. These values are not saved to the object.
            extend (list): A list of phrases to extend the current values in order to generate this sql statement. The extension list are not incorporated into the object's list of phases.  """
        if not sep:
            sep = self.separator

        values = self.values
        if extend:
            values.extend(extend)

        sql = self.startlist_phrase(values.pop(0))

        for val in values:
            sql += self.inlist_phrase(val, sep)

        #
        # Apply any template rules
        #
        sql = self.apply_template_values(sql, self.template_values)
        if template_values:
            sql = self.apply_template_values(sql, template_values)

        return(sql)

    #
    #
    # The following are functions to support the processing and inclusion of phrases.
    #
    #
    def startlist_phrase(self, val):
        """ This is called to format the first value for the output/sql. """
        if isinstance(val, Clause):
            return(val.startlist())
        elif isinstance(val, Query):
            return(val.startlist(label=val.label))
        elif type(val) in (list, tuple):
            return(val[0])
        return(val)

    def inlist_phrase(self, val, sep):
        """ This is called to format a non-first value for the output/sql. """
        if isinstance(val, Clause):
            return(val.inlist(sep))
        else:
            return(sep + val)

    def inlist(self, sep):
        """ This is called when *this* clause is composed within another clause and needs to return output/sql in that context. """
        return(sep + self.sql())

    def startlist(self):
        """ This is called when *this* clause begins the list of another clause and needs to return sql in that context """
        return(self.sql())

    #
    # The following are functions to allow the Clause to follow array-like behaviors.
    #
    def insert(self, position, value):
        """ Add a single value to the phrase list at the specific position """
        self._values.insert(position, value)

    def insert_list(self, position, values):
        """ Add a list of values to the phrase list starting at the specified position """
        for i, value in enumerate(values):
            self._values.insert(position, value)

    def pop(self, i=None):
        """ Pops an item from the list of phrases. """
        if i is not None:
            return(self._values.pop(i))
        else:
            # default is default pop
            return(self._values.pop())

    def prepend(self, value):
        """ Add a single value to the beginning the list  of phrases. """
        self.insert(0, value)

    def prepend_list(self, values):
        """ Add a list of values to the beginning the list  of phrases. """
        self.insert_list(0, values)

    def append(self, value):
        """ Add a single value to the list of phrases for this clause """
        self.extend([value])

    def extend(self, values):
        """ Add a list of values to the list of phrases for this clause """
        self._values.extend(values)

    def __setitem__(self, i, new_value):
        """ Array-ish function to facilitate indexed setting, i.e. clause_obj[2] = 'new phrase'. """
        if i < len(self._values):
            self._values[i] = new_value
        else:
            self._suffix[i - len(self._values)] = new_value

    def __getitem__(self, i):
        """ Array-ish function to facilitate indexed gets, i.e. print(clause_obj[2]) """
        if type(i) is int:
            if i < len(self._values):
                return(self.values[i])
            else:
                return(self._suffix[i - len(self._values)])

        # anything else should be a slice
        if i.start:
            start = i.start
        else:
            start = 0

        if i.stop:
            stop = i.stop
        else:
            stop = len(self._values) + len(self._suffix)

        if stop <= len(self._values):
            return(self.values[start:stop])
        elif start < len(self._values):
            return(self.values[start:] + self._suffix[:stop - len(self._values)])
        else:
            return(self._suffix[start - len(self._values):stop - len(self._values)])

    def __delitem__(self, i):
        """ Array-ish function to facilitate indexed deletes, i.e. del clause_obj[2] """
        if i < len(self._values):
            del self._values[i]
        else:
            del self._suffix[i - len(self._values)]

    @classmethod
    def remove_from_array(cls, array, value):
        """ Removes a specific value (case insensitive) from the provided array in-place, anywhere it appears. At present, this will recurse through lists but not through subsidiary clauses or queries. """
        i = 0
        while i < len(array):
            if type(array[i]) is list:
                cls.remove_from_array(array[i], value)
            elif type(array[i]) is str and array[i].lower() == value.lower():
                del array[i]
                # do not increment
                continue
            i += 1
        return

class SelectClause(Clause):
    """ Subclass of Clause for Select SQL clauses. """

    def extend(self, values):
        # We override the default extend to flatten arrays of arrays
        flattened = []
        for value in values:
            if type(value) in (list, tuple):
                flattened.extend(value)
            else:
                flattened.append(value)
        super().extend(flattened)


class WhereClause(Clause):
    """ Subclass of Clause for WHERE SQL clauses. """
    default_separator = "\n\tAND "



class TableClause(Clause):
    """ Subclass of Clause for FROM SQL clauses. """

    def __init__(self, *args, left_join=False, join_type=None, join_condition=None, **kwargs):
        """ Override init to handle alternate join types.

        Args:
            join_condition (str|list, optional): Indicate the default conditions with which to join this table clause (or at least, the first phrase of this table clause) when it is composed within a larger clause. If the clause is the first element (ie. it is applied using startlist instead of inlist), this is never used.
            join_type (str, optional): Indicates the type of join if this clause is composed within a larger clause. Not used if the clause stands alone or starts the larger clause. Default is 'JOIN'.
            left_join (bool): Shorthand to set the join_type to a 'LEFT JOIN', if True. Default is False.
            """

        self.join_type = join_type
        if left_join:
            self.left_join = True
        self.join_condition = join_condition
        super().__init__(*args, **kwargs)

    @property
    def default_separator(self):
        """ Overrides the default_separator parameter of the superclass to be dynamic based on the join type. """
        return(f"\n\t{self.join_type} ")

    @property
    def separator(self):
        """ Overrides the separator parameter of the superclass to be dynamic based on the join type. """
        return("\n\t" + self.join_type + " ")

    @property
    def left_join(self):
        """ bool: returns whether the clause will join a a LEFT JOIN. The setter will set the join to LEFT (or unset LEfT in favor of a regular join)."""
        return(self.join_type == 'LEFT JOIN')

    @left_join.setter
    def left_join(self, is_left):
        if is_left:
            self.join_type = 'LEFT JOIN'
        else:
            self.join_type = None
        return(self)

    @property
    def join_type(self):
        """ str: returns or sets the current join type """
        if self._join_type:
            return(self._join_type)
        else:
            return('JOIN')

    @join_type.setter
    def join_type(self, join_type):
        self._join_type = join_type

    def replace(self, to_replace, replace_with):
        """ Extends the superclass replace to also apply replacements to the join condition(s). """
        super().replace(to_replace, replace_with)
        rex = re.compile(to_replace)
        if not self.join_condition:
            return
        if type(self.join_condition) in (list, tuple):
            self.join_condition = [rex.sub(replace_with, elem) for elem in self.join_condition]
        else:
            self.join_condition = rex.sub(replace_with, self.join_condition)

    def add_join_condition(self, *conditions):
        """ Appends new conditions to the existing join condition(s). """
        dereference = len(conditions) == 1 and type(conditions[0]) in (list, tuple)
        if not self.join_condition:
            if dereference:
                self.join_condition = conditions[0]
            else:
                self.join_condition = conditions
        elif type(self.join_condition) in (list, tuple):
            if dereference:
                self.join_condition.extend(conditions[0])
            else:
                self.join_condition.extend(conditions)
        else:
            # join condition is not an array yet
            if dereference:
                self.join_condition = [self.join_condition] + list(conditions[0])
            else:
                self.join_condition = [self.join_condition] + list(conditions)


    def copy(self, join_condition=None, left_join=None, extend_join_condition=None, **kwargs):
        """ Extends the superclass copy to account for new join conditions.
        Args:
            extend_join_condition (list, optional): If provided, adds the parameter phrases to the phrases within the new copy.
            join_condition (list, optional): If provided, sets the join_condition for the copy to this parameter. The join_condition on the source object is ignored.
            left_join (bool, optional): Facilitates quickly making copies of table clauses that only differ in their left-joinedness. If specified, explicitly sets the left_join value on the copy.
            All other args and keywords are passed to the superclass.
        """
        new_clause = super().copy(**kwargs)
        if join_condition:
            new_clause.join_condition = join_condition
        elif extend_join_condition:
            new_clause.add_join_condition(extend_join_condition)
        if left_join is not None:
            new_clause.left_join = left_join
        return(new_clause)

    def join(self, *clauses, join_condition=None, left_join=None):
        """ Create a new TableClause that composes the current clause with the attached ones. Note that this creates a copy of the original clause, so modification will be propogate to other downstream objects.

        Args:
            clauses (list): The new clauses to combine with in the returned clause.
            join_condition (list, optional): specifies the join condition that will be used between the copy of the current object and the clauses that are joined to it. If not provided, join logic will be based on the clasues to be joined to.
            left_join (bool, optional): indicates that the clauses should be appended to the current object via left join (or not-left join, if explicitly set to False).
        Returns:
            a sqltemplate.TableClause object that combines self with the provided clauses (and the provided clauses are joined with a [left_join] and by [join_condition], if those parameters are specified).
        """

        new_clause = self.copy()
        if clauses:
            if isinstance(clauses[0], TableClause):
                new_clause.append(clauses[0].copy(join_condition=join_condition, left_join=left_join))
            elif left_join is not None:
                new_clause.append(TableClause(clauses[0], left_join=left_join, join_condition=join_condition))
            else:
                new_clause.append(clauses[0])

            new_clause.extend(clauses[1:])
        return(new_clause)

    def as_exists(self, negate=False, extend_condition=None):
        """ Turns the clause into an EXISTS statement to determine if any rows exist in the Table. The exists statement will be approximately "EXISTS (select 1 from <TABLE_CLAUSE> where <JOIN_CONDITION> AND <EXTEND_CONDITION>)"

        The JOIN_CONDITION for the original clause will be translated into the WHERE clause of the EXIST statement.

        Args:
            negate (bool): If True, return a NOT EXISTS statement. Default is False.
            extend_condition (str|list, optional): If provided, adds additional conditions to resolve the WHERE clause of the exist statement.
                 """

        if negate:
            sql = "NOT "
        else:
            sql = ""

        sql += "EXISTS (SELECT 1 FROM " + self.sql() + "\n\t WHERE\n\t\t"

        if type(extend_condition) is str:
            extend_condition = [extend_condition]

        # add the join condition
        if self.join_condition:
            if type(self.join_condition) in (list, tuple):
                conditions = self.join_condition.copy()
            else:
                conditions = [ self.join_condition ]
            if extend_condition:
                conditions.extend(flatten(extend_condition))
        elif extend_condition:
            conditions = flatten(extend_condition)
        else:
            raise Exception(f"Cannot turn a TableClause into an EXISTS substatement unless there is a join_condition. Attempted to call 'as_exists' on {self} (object with values: {self.values}) ")

        sql += "\n\t\tAND ".join(conditions)
        sql += "\n)"
        return(sql)

    def inlist_phrase(self, val, sep):
        """ This overrides the superclass inlist_phrase in order to handle the join condition formatting.

        Args:
            val (sqltemplate.Clause|sqltemplate.Query|list|str): The phrase/set to create an inlist string as output.
            sep (str): The separator
        Returns:
            str: A sql string for the phrase or set of phrases provided and separated by the provided sep. This will also apply any template substitions.
         """
        if isinstance(val, Clause):
            sql = val.inlist("\n\t" + val.join_type + " ")
        elif isinstance(val, Query):
            sql = "\n\t" + val.join_type + " " + val.as_join()
        elif type(val) not in (tuple, list):
            raise Exception("No condition on the table clause '"+str(val)+"' even though it is not the first table!")
        else:
            if isinstance(val[0], Clause):
                return(val[0].copy(join_condition=val[1]).inlist(sep))
            elif isinstance(val[0], Query):
                q = val[0]
                if len(val) > 1:
                    q = q.copy()
                    q.add_join_condition(val[1])
                elif not q.join_condition:
                    raise Exception("Query provided in the middle of a TableClause but has no join condition")
                return(sep + q.as_join())

            if type(val[1]) is str:
                sql = sep + val[0] + " ON " + val[1]
            else:
                sql = sep + val[0] + " ON " + " AND ".join(val[1])

        return(self.apply_template_values(sql, self.template_values))

    def inlist(self, sep):
        """ This overrides the superclass inlist in order to handle the join condition formatting.

        Args:
            sep (str): The separator
        Returns:
            str: A sql string for the the phrases encapsulated in the object and separated by the provided sep.
         """
        if self.join_condition:
            sql = self.inlist_phrase([self.values[0], self.join_condition], sep)
        elif type(self.values[0]) in (list, tuple):
            sql = self.inlist_phrase([self.values[0][0], self.values[0][1]], sep)
        else:
            raise Exception("Table Clause called composed within a list, but does not have a join condition!")

        if len(self.values) > 1:
            for val in self.values[1:]:
                sql += self.inlist_phrase(val, sep)
        return(self.apply_template_values(sql, self.template_values))

from .query import Query
