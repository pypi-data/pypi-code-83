# -*- coding: utf-8 -*-

from sql.aggregate import Aggregate

__all__ = ['AggregateExtra', 'StringAgg']

class AggregateExtra:
    """ adds a class variable
    """
    def __init__(self):
        self.separator = ''

# end AggregateExtra



class StringAgg(Aggregate, AggregateExtra):
    """ Links the records of a text column in a group-by-clause to a result column.
        Syntax: StringAgg(<column>, <separator>, [order])
    """
    __slots__ = ()
    _sql = 'STRING_AGG'

    def __init__(self, expression, separator, order=None):
        super(StringAgg, self).__init__(expression)
        self.separator = separator
        self.order1 = order

    def __str__(self):
        order_by = ''
        if self.order1:
            order_by = ' ORDER BY %s' % self.order1
        return "%s(%s, '%s'%s)" % (self._sql, self.expression, self.separator, order_by)

# end StringAgg
