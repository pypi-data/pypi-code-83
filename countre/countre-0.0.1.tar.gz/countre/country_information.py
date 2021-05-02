import re

from countre.regex_dict import regex_dict

# Import dictionary of country information named regex_dict which is
# stored in the file regex_dict.py.
regex_dict = regex_dict

regex_dict_index = {
    'country': 0,
    'sovereign': 1,
    'iso2': 2,
    'iso3': 3,
    'iso_num': 4,
    'ccTLD': 5,
    'calling_code': 6,
    'latitude': 7,
    'longitude': 8,
    'continent': 9,
    'sub_region': 10,
    'flag': 11,
    'total_area': 12,
    'land_area': 13,
    'water_area': 14,
    'capital': 15,
    'capital_latitude_sexa': 16,
    'capital_longitude_sexa': 17,
    'capital_longitude': 18,
    'capital_latitude': 19,
    'population_2019': 20,
    'gdp_2019': 21,
    'gdp_per_capita_2019': 22,
    'gdp_per_capita_ppp_2019': 23,
    'OECD': 24,
    'EU': 25,
    'EU_EEA': 26
}

def country_info(country_list, variables, no_match='no match'):
    '''
    Returns variables for each country in either a list or dictionary.

    Parameters:
        country_list (list) : list of country names, iso2 or iso3
                              codes to get variables for.

        variables (str, list) : choose one or more from the following
            {'country', 'population_2019', 'iso2', 'iso3', 'iso_num',
             'calling_code', 'latitude', 'longitude', 'ccTLD', 'flag',
             'capital', 'continent', 'sub_region', 'sovereign',
             'OECD', 'EU', 'EU_EEA', 'flag',
             'capital_latitude_sexa', 'capital_longitude_sexa',
             'capital_longitude', 'capital_latitude', 'gdp_2019',
             'gdp_per_capita_2019', 'gdp_per_capita_ppp_2019',
            'total_area', 'land_area', 'water_area'}

        no_match (str) : value returned for a country if there is no
                         match. Default: 'no match'.

    Returns:
        list of values if only one variable given.
        dictionary of values if more than one varibale is given.
    '''

    if type(variables) == str:
        index = regex_dict_index[variables]
        variable_list = []
        for country in country_list:
            match = no_match
            for regex_pattern in regex_dict:
                if bool(re.match(regex_pattern, country, re.IGNORECASE)):
                    match = regex_dict[regex_pattern][index]
                    break
            variable_list.append(match)
        return variable_list

    else:
        indices = [regex_dict_index[v] for v in variables]
        variables_dict = {}
        for i, v in zip(indices, variables):
            variables_dict[v] = []
            for country in country_list:
                match=no_match
                for regex_pattern in regex_dict:
                    if bool(re.match(regex_pattern, country, re.IGNORECASE)):
                        match = regex_dict[regex_pattern][i]
                        break
                variables_dict[v].append(match)
        return variables_dict


eu_members = {}
for c in regex_dict:
    if regex_dict[c][regex_dict_index['EU']] == True:
        eu_members[c] = [regex_dict[c][regex_dict_index['country']],
                         regex_dict[c][regex_dict_index['iso2']],
                         regex_dict[c][regex_dict_index['iso3']]]

eu_member_index = {
    'country': 0,
    'iso2': 1,
    'iso3': 2
}

def eu_27(code='country'):
    """
    Return a list containing the country names, iso2 or iso3 codes for
    the 27 EU members.

    Parameters:
        code (str) : {'country', 'iso2', 'iso3'}

    Returns:
        list of 27 names, iso2 or iso3 codes.
    """
    index = eu_member_index[code]
    variable_list = []
    for country in eu_members:
        variable_list.append(eu_members[country][index])
    return variable_list


oecd_members = {}
oecd_members = {}
for c in regex_dict:
    if regex_dict[c][regex_dict_index['OECD']] == True:
        oecd_members[c] = [regex_dict[c][regex_dict_index['country']],
                           regex_dict[c][regex_dict_index['iso2']],
                           regex_dict[c][regex_dict_index['iso3']]]

oecd_member_index = {
    'country': 0,
    'iso2': 1,
    'iso3': 2
}

def oecd(code='country'):
    """
    Return a list containing the country names, iso2 or iso3 codes for
    the 37 OECD members.

    Parameters:
        code (str) : {'country', 'iso2', 'iso3'}

    Returns:
        list of 37 names, iso2 or iso3 codes.
    """
    index = oecd_member_index[code]
    variable_list = []
    for country in oecd_members:
        variable_list.append(oecd_members[country][index])
    return variable_list
