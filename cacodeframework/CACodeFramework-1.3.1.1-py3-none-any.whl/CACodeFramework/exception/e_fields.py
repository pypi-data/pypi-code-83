<<<<<<< HEAD
JSON_ERROR = 'CACode-Json'
SYNTAX_ERROR = 'CACode-Syntax'
ATTR_ERROR = 'CACode-Attr'
LOG_OPERA_NAME = 'CACode-Database-Operation'
WARN = 'WARN'
INFO = 'INFO'
DB_TASK = 'DATABASE OPERATION'
PARSE_ERROR = 'CACode-Parse'
=======
def mat(prefix, suffix):
    return '%s:%s' % (prefix, suffix)


def CACode_SqlError(msg):
    return mat('CACode-SqlError', msg)


def CACode_Factory_Error(msg):
    return mat('CACode-Factory', msg)


def Json_Error(msg):
    return mat('CACode-Json', msg)


def Syntax_Error(msg):
    return mat('CACode-SyntaxError', msg)


def Attribute_Error(msg):
    return mat('CACode-AttributeError', msg)


def Log_Opera_Name(msg):
    return mat('CACode-DatabaseOperation', msg)


def Miss_Attr(msg):
    return mat('CACode-Attribute', msg)


def Error():
    return 'ERROR'


def Warn():
    return 'WARNING'


def Info():
    return 'INFO'


def Database_Operation():
    return 'DATABASE OPERATION'


def Parse_Error(msg):
    return mat('CACode-Parse', msg)


class FieldNotExist(AttributeError):
    pass
>>>>>>> test
