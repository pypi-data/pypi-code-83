# import classes into the googleapps namespace
from googleapps.service import ServiceManager
from googleapps.serviceclient import ServiceClient
from googleapps.base import *

# import core api modules
import googleapps.sheets
import googleapps.drive

import re
import datetime, time

# requires apiclient, oauth2client, google-api-python-client

""" googleapps

This module provides a suite of encapsulations of API access to Google Apps that attempt to follow encapsulation expectations for good object-oriented (and Python) code, as much as possible. So, instead of the user needing to parse Google API references (https://developers.google.com/apis-explorer/) or rely on individual wrappers that encapsulate single APIs, this library seeks to:
1. Provide a consistent set of base packages to access the API and generate low-level but object-oriented codebooks
2. Provide a system to build well encapsulated systems upon it
3. Implement core APIs that I use into this sytem (ie. drive, sheets, and gmail at the time of this documentation)

Also, because rapid development (for me) often starts off by creating local versions that I realize are better off in the Google ecosystem, I follow the following Guidelines in module development:
- Use naming conventions and functional encapsulation that parallels common local-source alternatives so that converting between one system and another (or maintaining local and remote options) requires as little work for the coder as possible.
- In line with #1, if the Google API is conceptually different, follow local module naming conventions for the core googleapps module and provide an additional function that follows the Google API encapsulation, so that developers familiar with the Google reference can work seemlessly
"""

parens = re.compile(r'_(\w)')
humps = re.compile(r'([a-z])([A-Z0-9]+)')
numletter = re.compile(r'(\d)([a-zA-Z]+)')
acronym = re.compile(r'([A-Z]+)([A-Z][a-z\d])')

def toCamel(string:str) -> str:
    """ convert snake_case into camelCase. (Note: this is not purely reciprocal with fromCamel because there is a loss of resolution of uppercase acronyms in the conversion to snake case)"""
    return(parens.sub(lambda m: m.group(1).upper(), string.strip()))

def fromCamel(string:str) -> str:
    """ convert camelCase into snake_case """
    string = humps.sub(lambda m: m.group(1) + '_' + m.group(2), string.strip())
    string = numletter.sub(lambda m: m.group(1) + '_' + m.group(2), string)
    string = acronym.sub(lambda m: m.group(1) + '_' + m.group(2), string)
    return(string.lower())

def unCamel(json:dict, flatten=False) -> dict:
    """ Take an arbitrary data structure with camelCase keys and turn it into a snake_case python data structure. The most frequent use case is when receiving json from Google API calls.
    TODO: Resolve whether integer-looking keys should be remapped to actual integers (since json requires all keys to be strings. I'm not convinced this is actually ever a priority in the Google API case, but it is a major difference between the JSON spec and Python datastructures in general - so, be careful using this for purposes aside from parsing REST responses)

    Args:
        json (object): The data structure to unCamel.
        flatten (bool, optional): If true, do not not duplicate the nesting part of nested dictionaries, instead ignore the top-level key and move all bottom-level keys into the result tree.  Default is false.

    Examples:
        >>> print unCamel({'camelParamA': 12, 'camelParamB': [1,2,3], 'camelParamC': {'subCamelA': 1, 'subCamelB': 2}})
        {'camel_param_a': 12, 'camel_param_b': [1, 2, 3], 'camel_param_c': {'sub_camel_a': 1, 'sub_camel_b': 2}}

        >>> print unCamel({'camelParamA': 12, 'camelParamB': [1,2,3], 'camelParamC': {'subCamelA': 1, 'subCamelB': 2}}, flatten=True)
        {'camel_param_a': 12, 'camel_param_b': [1, 2, 3], 'sub_camel_a': 1, 'sub_camel_b': 2} # no 'camel_param_c'!!
    """
    if not json:
        return
    # handle non-dict types
    if type(json) in (list, tuple):
        return(list(map(lambda item: unCamel(item), json)))
    elif type(json) is not dict:
        return(json)

    # okay, expected json struct
    result = {}
    for key in json:
        if type(json[key]) is dict:
            subjson = unCamel(json[key], flatten)
            if flatten:
                result.update(subjson)
            else:
                result[fromCamel(key)] = subjson
        elif type(json[key]) in (list, tuple):
            # lists are possibly atomic
            # but they could also be json substructs
            # we figure that out by looking at the first element
            # if it's a dict, we process
            # else we don't
            new_key = fromCamel(key)
            if not len(json[key]) or type(json[key][0]) is not dict:
                result[new_key] = json[key]
            else:
                processed = list(map(lambda element: unCamel(element), json[key]))
                if flatten:
                    # this is a major problem, right?
                    raise Exception("This probalby shouldn't be allowed as it would likely overwrite itself")
                    for subjson in processed:
                        result.update(subjson)
                else:
                    result[new_key] = processed
        else:
            result[fromCamel(key)] = json[key]
    return(result)

def to_rfctime(datetimeobj) -> str:
    """ Converts a datetime.* object or unix epoch time to an RFC 3339 time string.

    Args:
        datetimeobj: One of the following (note that wihtout an explicit timezone, localtime is used):
            - a datetime.date or datetime.datetime object, which is directly converted (dates will return 00:00:00 as their time)
            - a datetime.time object, which is converted to using today at the given time. Use with caution.
            - an integer of float that represents unix epoch (local)time, the number of seconds since 1970-01-01 in the local timezone

    Returns: A string of the argument in RFC3339 format
    """
    t = type(datetimeobj)
    # -- handle epoch time and datetime.date recursively
    if t in (int, float):
        return(to_rfctime(datetime.datetime.fromtimestamp(datetimeobj)))
    elif t is datetime.date:
        return(to_rfctime(datetime.datetime(datetimeobj.year, datetimeobj.month, datetimeobj.day)))

    tzoffset = datetimeobj.utcoffset()

    def tzstring_from_seconds(seconds):
        difftime = seconds / 3600
        hours = int(difftime)
        if hours < 0:
            return(format(hours, '03d') + ':' + format(int((hours-difftime)*60), '02d'))
        else:
            return('+' + format(hours, '02d') + ':' + format(int((difftime-hours)*60), '02d'))

    if tzoffset is not None:
        secoffset = tzoffset.total_seconds()
        if secoffset == 0:
            tzstring = 'Z'
        else:
            # NOTE that secoffset from the datetime object will be negative for western hemisphere timezones!!
            tzstring = tzstring_from_seconds(secoffset)
    else:
        # set to LOCALTIME
        # NOTE THAT LOCALTIME offsets will be POSITIVE for western hemisphere timezones!!
        lt = time.localtime(datetimeobj.timestamp())
        # check for daylight savings time
        if lt.tm_isdst:
            tzstring = tzstring_from_seconds(-time.altzone)
        else:
            tzstring = tzstring_from_seconds(-time.timezone)

    if datetimeobj.microsecond:
        # we dont want a string that is T12:15:01.420000, so we reformat the microsecond argument
        ms = str(datetimeobj.microsecond / 1000000)[1:]
    else:
        ms = ''
    if t is datetime.datetime:
        return(datetimeobj.strftime("%Y-%m-%dT%H:%M:%S") + ms + tzstring)
    elif t is datetime.time:
        today = datetime.date.now()
        return(today.strftime("%Y-%m-%dT") + datetimeobj.strftime("%H:%M:%SZ"))
    elif t in (int, float):
        # assume it's an epoch timestamp
        return(to_rfctime(datetime.datetime.fromtimestamp(datetimeobj)))
    return        

rfcre = re.compile('([0-9]{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]+)?(([Zz])|(([\+|\-][01][0-9]|2[0-3]):([0-5][0-9])))')
def from_rfctime(rfcstring, require=False) -> datetime.datetime:
    """ Converts an RFC time string to a datetime.datetime object.

    Args:
        rfcstring (str): The string to convert into a datetime object. Note that if require is False, the type is not checked.
        require (bool): If true, guarantees that the function returns a datetime object or throws an exception. This allows the user to avoid third-party input verification.
    Return:
        None if rfcstring is not a string in rfc format
    """
    if not type(rfcstring) is str:
        if require:
            raise ValueError("Input to from_rfctime is not a string, it is " + str(type(rfcstring)) )
        return
    m = rfcre.fullmatch(rfcstring)
    if not m:
        if require:
            raise ValueError("Input '"+rfcstring+"' to from_rfctime is not in RFC3334 format" )
        return

    parts = m.groups()
    # convert the regex match to integers
    params = [int(x) for x in parts[:6]]

    # resolve mseconds
    if parts[6] is not None:
        params.append(int(float(parts[6])*1000000))

    if parts[7] == 'Z':
        # utc timezone
        return(datetime.datetime(*params, tzinfo=datetime.timezone.utc))
    else:
        # convert to local timezone
        hours = int(parts[10])
        minutes = int(parts[11])
        return(datetime.datetime(*params, tzinfo=datetime.timezone(datetime.timedelta(hours=hours, minutes=minutes))))

    # old logic
    #match = rfcre.match(rfcstring)
    #if not match:
    #    raise Exception("Expected string in RFC format, but this did not match the regex: " + str(rfcstring))
    #rfc = match.groups()
    #return(datetime.datetime(*[int(x) for x in [*rfc[0:5], rfc[6]]]))

def json_fieldmask(json):
    """ Converts a dict with nested dict objects into a list in which nested keys are appended to the parent key with a dot. The general use case is when the Google API requests a list of fields and the user wishes to autogenerate the fields as exactly the parameters set in a python object that is going to be sent.

    Example:
        >>>json_fieldmask({'ParamA': 12, 'ParamB': [1,2,3], 'ParamC': {'subA': 1, 'subB': 2}})
        ['ParamA',
         'ParamB',
         'ParamC.subA',
         'ParamC.subB']
        """
    fields = []
    for field in json:
        if type(json[field]) is dict:
            subfields = json_fieldmask(json[field])
            fields.extend([ '.'.join([field, sf]) for sf in subfields ])
        else:
            fields.append(field)
    return(fields)
