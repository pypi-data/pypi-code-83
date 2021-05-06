def parse(table_class: type):
    return table_class.db + "." + table_class.__name__
