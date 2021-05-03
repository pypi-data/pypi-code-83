# file sqltemplate/query.py

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

from .clause import *
from .sqlcore import SQLCore


class Query(SQLCore):
    """ An encapsulation for a full SQL query.

    Args:
        select (str|list|sqltemplate.Clause): The SELECT clause
        tables (str|list|sqltemplate.Clause): The FROM clause
        where (str|list|sqltemplate.Clause): The WHERE clause
        group (str|list|sqltemplate.Clause): The GROUP BY Clause
        order (str|list|sqltemplate.Clause): The ORDER BY Clause
        having (str|list|sqltemplate.Clause): The HAVING Clause
        distinct (bool): If True, applies to DISTINCT keyword prior to the SELECT clause.
        auto_group (bool): If True, generates the GROUP BY clause based on the SELECT using the sqltemplate.clause.make_group_from_select() function. Used so you don't have to manually specify the group by if it is simply all of the non-aggregate phrases of the SELECT clause.
        oracle_hint (str, optional): Specifies an Oracle style hint to be applied at the beginning of the SELECT clause.  oracle=hint="indexed" will lead to the query to begin "SELECT /*+ INDEXED */ "....
        name (str, optional): A name for the query object. This is not explicitly used within the sqltemplate package
        template_values (dict, optional): A mapping of default template values to apply if the query is texualized.
        label (str, optional): A label for the Query if it is applied as an inline view
        join_condition (list|str, optional): A list of conditions for the Query if it is applied as an inline view.
        join_type (str, optional): The type of join that the Query should be joined with with an existing query as an inline view. Default is 'JOIN'
        left_join (boolean): Shorthand to set the join_type to 'LEFT JOIN' if True. Default is False.
        exists_condition (list|str, optional): A list of conditions to be added to the WHERE statement if the Query is applied in EXISTS context.
    """
    def __init__(self, select, tables, where=None, group=None, order=None, having=None, name=None, template_values=None, label=None, join_condition=None, left_join=None, join_type=None, exists_condition=None, distinct=False, auto_group=False, oracle_hint=False):
        super().__init__(template_values=template_values)

        self.auto_group = auto_group
        self.distinct = distinct
        self.oracle_hint = oracle_hint
        self.label = label
        self.name = name

        self.select = select
        self.tables = tables
        self.where = where
        self.group = group
        self.order = order
        self.having = having

        self.join_condition = join_condition
        self.join_type = join_type
        if left_join is not None:
            self.left_join = left_join
        self.exists_condition = exists_condition

        self._set_operations = []

    @property
    def select(self):
        """ Accessor for the SELECT clause. """
        return(self._select)

    @select.setter
    def select(self, select):
        if not select:
            raise Exception('Queries must have a select clause')
        if isinstance(select, SelectClause):
            self._select = select
        elif type(select) in (list, tuple):
            self._select = SelectClause(*select)
        else:
            self._select = SelectClause(select)

    @property
    def tables(self):
        """ Accessor for the FROM/TABLES clause. """
        return(self._tables)

    @tables.setter
    def tables(self, tables):
        if not tables :
            raise Exception('Queries must have a tables clause')
        if isinstance(tables, TableClause):
            self._tables = tables
        elif type(tables) in (list, tuple):
            self._tables = TableClause(*tables)
        else:
            self._tables = TableClause(tables)

    @property
    def where(self):
        """ Accessor for the WHERE clause. """
        return(self._where)

    @where.setter
    def where(self, where):
        if not where:
            self._where = None
        elif isinstance(where, Clause):
            self._where = where
        elif type(where) in (list, tuple):
            self._where = WhereClause(*where)
        else:
            self._where = WhereClause(where)

    @property
    def group(self):
        """ Accessor for the GROUP BY clause. """
        if not self._group:
            if self.auto_group:
                self._group = Clause(*make_group_from_select(self.select))
        return(self._group)

    @group.setter
    def group(self, group):
        if not group:
            self._group = None
        elif isinstance(group, Clause):
            self._group = group
        elif type(group) in (list, tuple):
            self._group = Clause(*group)
        else:
            self._group = Clause(group)


    @property
    def order(self):
        """ Accessor for the ORDER BY clause. """
        return(self._order)

    @order.setter
    def order(self, order):
        if not order:
            self._order = None
        elif isinstance(order, Clause):
            self._order = order
        elif type(order) in (list, tuple):
            self._order = Clause(*order)
        else:
            self._order = Clause(order)


    @property
    def having(self):
        """ Accessor for the HAVING clause. """
        return(self._having)

    @having.setter
    def having(self, having):
        if not having:
            self._having = None
        elif isinstance(having, Clause):
            self._having = having
        elif type(having) in (list, tuple):
            self._having = WhereClause(*having)
        else:
            self._having = WhereClause(having)

    @property
    def join_type(self):
        """ The join_type is used when the query is called in list context as an inline view, and indicates how the view that represents this query will be joined to to the preceding phrase.  By Default, this is simply 'JOIN'  """
        if self._join_type:
            return(self._join_type)
        else:
            return('JOIN')

    @join_type.setter
    def join_type(self, join_type):
        self._join_type = join_type

    @property
    def left_join(self):
        """ bool: left_join is another interface to the join_type that considers the common case where a join is either a standard inner join or a left inner join.  Returns True if the current join_type is LEFT JOIN and false otherwise.

        Similarly, the setter takes in a boolean and sets the join type to 'LEFT JOIN' if true and just 'JOIN' otherwise. """
        return(self.join_type == 'LEFT JOIN')

    @left_join.setter
    def left_join(self, is_left):
        if is_left:
            self.join_type = 'LEFT JOIN'
        else:
            self.join_type = 'JOIN'

    @property
    def name(self):
        """ str: Provides the name for the Query, is available. If not set and label is set, it will provide the label. """
        if not self._name and self.label:
            return(self.label)
        return(self._name)

    @name.setter
    def name(self, name):
        self._name = name


    @property
    def label(self):
        """str: The label for the inline view when the Query is called in such a context. If the label contains a templated element, the accessor will return the string already substituted with the template values, provided they've been defined."""
        if not self._label:
            return
        if self.template_values:
            label = self.apply_template_values(self._label, self.template_values)
        else:
            label = self._label
        return(label)

    @label.setter
    def label(self, label):
        self._label = label


    @property
    def set_operations(self):
        """ list(tuple): For composite queries, the set operations are the subsequent queries such that each element is a 2-element tuple of the operation (union, intersect, minus) and the query relevant for the operations. """
        return(self._set_operations)

    def union(self, query):
        """ Adds a new UNION-based query to the list of set-operated queries that this query is combined with."""
        if type(query) in (list, tuple):
            self._set_operations.extend([ ('union', subq) for subq in query ] )
        else:
            self._set_operations.append( ('union', query ) )

    def intersect(self, query):
        """ Adds a new INTERSECTION-based query to the list of set-operated queries that this query is combined with."""
        if type(query) in (list, tuple):
            self._set_operations.extend([ ('intersect', subq) for subq in query ] )
        else:
            self._set_operations.append( ('intersect', query ) )

    def minus(self, query):
        """ Adds a new MINUS-based query to the list of set-operated queries that this query is combined with."""
        if type(query) in (list, tuple):
            self._set_operations.extend([ ('minus', subq) for subq in query ] )
        else:
            self._set_operations.append( ('minus', query ) )

    @property
    def join_condition(self):
        """list: the clause by which to join an inline view with this query object.  """
        if self._join_condition and self.template_values:
            return(self.apply_template_values(self._join_condition, self.template_values))
        else:
            return(self._join_condition)

    @join_condition.setter
    def join_condition(self, join_condition):
        if join_condition is None:
            self._join_condition = None
        elif type(join_condition) is not list:
            self._join_condition = [join_condition]
        else:
            self._join_condition = join_condition


    def add_join_condition(self, addl_conditions):
        """Additional conditions to extend the current join condition(s). """
        if type(addl_conditions) is list:
            self._join_condition.extend(addl_conditions)
        else:
            self._join_condition.append(addl_conditions)


    @property
    def exists_condition(self):
        """list: A clause or clauses that are appended to the WHERE clause when this query object is called within EXISTS context.  """
        if not self._exists_condition:
            return
        if self.template_values:
            return(self.apply_template_values(self._exists_condition, self.template_values))
        else:
            return(self._exists_condition)

    @exists_condition.setter
    def exists_condition(self, exists_condition):
        if exists_condition is None:
            self._exists_condition = None
        elif type(exists_condition) is not list:
            self._exists_condition = [exists_condition]
        else:
            self._exists_condition = exists_condition


    def add_exists_condition(self, addl_conditions):
        """object|list: Additional conditions to extend the current exists_condition(s). """
        if type(addl_conditions) is list:
            self._exists_condition.extend(addl_conditions)
        else:
            self._exists_condition.append(addl_conditions)


    def sql(self, template_values=None, extend_select=None, extend_where=None):
        """ Returns a string with the current SQL query based on the object.

        Args:
            template_values(dict, optional): Additional template values to apply during the generation of the sql. These will not persist in the object after the immediate call.
            extend_select (list, optional): Additional phrases for the SELECT clause to apply during the generation of the sql. These will not persist in the object after the immediate call.
            extend_where (list, optional): Additional phrases for the WHERE clause to apply during the generation of the sql. These will not persist in the object after the immediate call.
        """

        sql = "SELECT"

        if self.oracle_hint:
            if type(self.oracle_hint) is list:
                sql += ' /*+' + ' '.join(self.oracle_hint) + ' */'
            else:
                sql += f' /*+ {self.oracle_hint} */'

        if self.distinct:
            sql += " DISTINCT"

        sql += "\n\t" + self.select.sql(extend=extend_select)

        sql += "\nFROM\n\t" + self.tables.sql()

        if self.where:
            sql += "\nWHERE\n\t" + self.where.sql(extend=extend_where)
        elif extend_where:
            sql += "\nWHERE\n\t" + WhereClause(extend_where).sql()

        if self.group:
            sql += "\nGROUP BY\n\t" + self.group.sql()

        if self.having:
            sql += "\nHAVING\n\t" + self.having.sql()

        if self.order:
            sql += "\nORDER BY\n\t" + self.order.sql()


        #
        # Apply any additional query set operations - in this case, only other sqltemplate objects can be provided
        #
        if self.set_operations:
            for operand, query in self.set_operations:
                sql += f"\n{operand}\n" + query.sql()

        #
        # Apply any template rules
        #
        if self.template_values:
            sql = self.apply_template_values(sql, self.template_values)

        if template_values:
            sql = self.apply_template_values(sql, template_values)

        return(sql)

    def as_exists(self, negate=False, extend_condition=None, **sqlparams):
        """
        Returns a SQL string for an EXISTS clause in which the conditions of this query make up the parts of the exists. By default, it uses the object's exists_conditions, which may be supplemented.
        Args:
            negate (bool): creates a NOT EXISTS clause.
            extend_condition (str|list): override the query's join_condition with the provided value. To simply ignore the query's current join condition, pass in a non-None but false value, i.e. 0 or False.
            sqlparams: Any additional keyword arguments will be passed to the subquery() call
        """
        if extend_condition:
            extend_where = extend_condition.copy() # so we don't change the user's array
        else:
            extend_where = []

        if self.exists_condition:
            extend_where.extend(self.exists_condition)

        sql = "EXISTS " + self.copy(
            select=['1'],
            extend_where=extend_where,
        ).subquery(**sqlparams)

        if negate:
            sql = ("NOT " + sql)
        return(sql)

    def as_join(self, label=None, extend_condition=None, join_condition=None):
        """ Return a SQL string for this Query as an inline view that can be joined to other tables in a larger Query. If no join conditions exist, either as parameters or instance variables, an error is thrown.
        Args:
            label (str,optional): Specifies the name for the inline view. If not provided, uses the self.label instance variable. If self.label does not exist, raises an error.
            join_condition(list, optional): Sets the join condition for the returned SQL. This overrides the existing/default join condition, if it exists, but this will not persist in the object beyond this function.
            extend_condition(list, optional): Appends the provided phrases to the existing/default join condition, but this will not persist in the object beyond this function.
        """
        # turn it into a subquery with the join condition
        if not label:
            if not self.label:
                raise Exception("Query object included as a table in another object. This would normally create an inline view BUT no 'label' defined on the subquery!")
            label = self.label

        if join_condition:
            all_condition = join_condition.copy()
        elif self.join_condition:
            all_condition = self.join_condition.copy()
        else:
            all_condition = []

        if extend_condition:
            all_condition.append(extend_condition)

        if not all_condition:
            raise Exception("Query object included as a table in another object. This would normally create an inline view BUT no 'join_condition' defined subquery!")

        return(self.startlist() + ' ON ' + ' AND '.join(all_condition))

    def subquery(self, **sqlparams):
        """ Returns the SQL for the query wrapped in a parenthetical phrase suitable to inclusion as an inline view or an exists phrase, among others."""
        return("("+self.sql(**sqlparams).replace("\n", "\n\t")+"\n\t)")

    def startlist(self, label=None, **sqlparams):
        """ A version of the subquery call that aliases the subquery as the label (if it is provided as a parameter or exists as an instance vairable). The primary focus here is for use when the subquery is included in the FROM clause as an inline view. """
        if not label:
            label = self.label
        if label:
            return(self.subquery(**sqlparams) + f' {label}')
        else:
            return(self.subquery(**sqlparams))


    def inlist(self, **sqlparams):
        """ Formats the Query as an inline view with a label and the join conditions provided. """
        return(self.startlist())

    def replace(self, to_replace, replace_with):
        """ """
        #go through all of the template rules and replace anything in the values
        rex = re.compile(to_replace)
        for template in self.template_values:
            if type(self.template_values[template]) is str:
                self.template_values[template] = rex.sub(replace_with, self.template_values[template])

        # go through all of the clauses and replace them
        for clause_name in ('select', 'tables', 'where', 'group', 'order', 'having', ):
            clause = getattr(self, clause_name)
            if clause:
                clause = clause.replace(to_replace, replace_with)

        for listclause_name in ('_join_condition', '_exists_condition'):
            listclause = getattr(self, listclause_name)
            if listclause:
                for i, clause in enumerate(listclause):
                    listclause[i] = clause.replace(to_replace, replace_with)

    def copy(self, extend_select=None, extend_tables=None, extend_where=None, extend_group=None, extend_having=None, extend_order=None, extend_join_condition=None, extend_exists_condition=None, auto_group=None, **kwargs):
        """ Extends superclass copy to more easily extend sqltemplate components safely - provides a deep copy of all clauses and subclauses so that any changes to the subsequent object to not change the source object.
        Args:
            extend_select, extend_tables, extend_where, extend_group, extend_having, extend_order (list|sqltemplate.SQLCore, optional): If provided, these will extend the core clauses of the copied query's with the new elements. The copy of the original will still be preserved.
            extend_join_condition, extend_exists_condition (list, optional): If provided, these will extend the copy of the source query's join exists conditions.
            auto_group (bool, optional): If specified, will set the auto_group field as specified, overriding whatever the source Query's value was.
            kwargs: All other keyword arguments are passed to the superclass.copy function all.
        """


        result = super().copy(**kwargs)
        if auto_group is None:
            result.auto_group = self.auto_group
        else:
            result.auto_group = auto_group

        if extend_select:
            result.select.extend(extend_select)
        if extend_tables:
            result.tables.extend(extend_tables)
        if extend_where:
            if not result.where:
                result.where = extend_where
            else:
                result.where.extend(extend_where)
        if extend_group:
            # extend the group
            if not result.group:
                result.group = extend_group
            else:
                result.group.extend(extend_group)
        elif self.auto_group or result.auto_group:
            # clear out any grouping that is an artifact of the source select
            result._group = None

        if extend_having:
            if not result.having:
                result.having = extend_having
            else:
                result.having.extend(extend_having)
        if extend_order:
            if not result.order:
                result.order = extend_order
            else:
                result.order.extend(extend_order)
        if extend_join_condition:
            result.add_join_condition(extend_join_condition)
        if extend_exists_condition:
            result.add_exists_condition(extend_exists_condition)
        return(result)


    def __str__(self):
        """ If attempting to print the clause, print the SQL"""
        return(self.sql())
