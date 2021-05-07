def normalize_list(value):
    if value == None:
        return []
    
    if type(value) is not list:
        return [value]
    else:
        return value
