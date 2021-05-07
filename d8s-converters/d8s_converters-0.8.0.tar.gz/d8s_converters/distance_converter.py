from .converter import convert

""" The code in this file was created from this code:
s = '''
def {{a}}_to_{{b}}({{a}}):
    return convert({{a}}, '{{a}}', '{{b}}')'''

# these time units (with 'meter' added) were taken from:
# https://github.com/hgrecco/pint/blob/ffc05dcf92347b217e14adbf96c36160f6128627/pint/default_en.txt
l = ['meter',
'centimeter',
'millimeter',
'kilometer',
'inch',
'hand',
'foot',
'yard',
'mile',
'light_year',
'astronomical_unit',
'parsec',
'nautical_mile',
'angstrom',
'micron',
'planck_length',]
l = pluralize(l)

funcs = []

for i in l:
    for j in l:
        if i == j:
            continue
        new_func = template_render(s, a=i, b=j)
        funcs.append(new_func)

for i in funcs:
    print(i)
    print('\n\n')

file_append('../democritus_core/distance_converter.py', '\n\n\n'.join(funcs))
"""


def meters_to_centimeters(meters):
    """Convert meters to centimeters."""
    return convert(meters, 'meters', 'centimeters')


def meters_to_millimeters(meters):
    """Convert meters to millimeters."""
    return convert(meters, 'meters', 'millimeters')


def meters_to_kilometers(meters):
    """Convert meters to kilometers."""
    return convert(meters, 'meters', 'kilometers')


def meters_to_inches(meters):
    """Convert meters to inches."""
    return convert(meters, 'meters', 'inches')


def meters_to_hands(meters):
    """Convert meters to hands."""
    return convert(meters, 'meters', 'hands')


def meters_to_feet(meters):
    """Convert meters to feet."""
    return convert(meters, 'meters', 'feet')


def meters_to_yards(meters):
    """Convert meters to yards."""
    return convert(meters, 'meters', 'yards')


def meters_to_miles(meters):
    """Convert meters to miles."""
    return convert(meters, 'meters', 'miles')


def meters_to_light_years(meters):
    """Convert meters to light years."""
    return convert(meters, 'meters', 'light_years')


def meters_to_astronomical_units(meters):
    """Convert meters to astronomical units."""
    return convert(meters, 'meters', 'astronomical_units')


def meters_to_parsecs(meters):
    """Convert meters to parsecs."""
    return convert(meters, 'meters', 'parsecs')


def meters_to_nautical_miles(meters):
    """Convert meters to nautical miles."""
    return convert(meters, 'meters', 'nautical_miles')


def meters_to_angstroms(meters):
    """Convert meters to angstroms."""
    return convert(meters, 'meters', 'angstroms')


def meters_to_microns(meters):
    """Convert meters to microns."""
    return convert(meters, 'meters', 'microns')


def meters_to_planck_lengths(meters):
    """Convert meters to planck lengths."""
    return convert(meters, 'meters', 'planck_lengths')


def centimeters_to_meters(centimeters):
    """Convert centimeters to meters."""
    return convert(centimeters, 'centimeters', 'meters')


def centimeters_to_millimeters(centimeters):
    """Convert centimeters to millimeters."""
    return convert(centimeters, 'centimeters', 'millimeters')


def centimeters_to_kilometers(centimeters):
    """Convert centimeters to kilometers."""
    return convert(centimeters, 'centimeters', 'kilometers')


def centimeters_to_inches(centimeters):
    """Convert centimeters to inches."""
    return convert(centimeters, 'centimeters', 'inches')


def centimeters_to_hands(centimeters):
    """Convert centimeters to hands."""
    return convert(centimeters, 'centimeters', 'hands')


def centimeters_to_feet(centimeters):
    """Convert centimeters to feet."""
    return convert(centimeters, 'centimeters', 'feet')


def centimeters_to_yards(centimeters):
    """Convert centimeters to yards."""
    return convert(centimeters, 'centimeters', 'yards')


def centimeters_to_miles(centimeters):
    """Convert centimeters to miles."""
    return convert(centimeters, 'centimeters', 'miles')


def centimeters_to_light_years(centimeters):
    """Convert centimeters to light years."""
    return convert(centimeters, 'centimeters', 'light_years')


def centimeters_to_astronomical_units(centimeters):
    """Convert centimeters to astronomical units."""
    return convert(centimeters, 'centimeters', 'astronomical_units')


def centimeters_to_parsecs(centimeters):
    """Convert centimeters to parsecs."""
    return convert(centimeters, 'centimeters', 'parsecs')


def centimeters_to_nautical_miles(centimeters):
    """Convert centimeters to nautical miles."""
    return convert(centimeters, 'centimeters', 'nautical_miles')


def centimeters_to_angstroms(centimeters):
    """Convert centimeters to angstroms."""
    return convert(centimeters, 'centimeters', 'angstroms')


def centimeters_to_microns(centimeters):
    """Convert centimeters to microns."""
    return convert(centimeters, 'centimeters', 'microns')


def centimeters_to_planck_lengths(centimeters):
    """Convert centimeters to planck lengths."""
    return convert(centimeters, 'centimeters', 'planck_lengths')


def millimeters_to_meters(millimeters):
    """Convert millimeters to meters."""
    return convert(millimeters, 'millimeters', 'meters')


def millimeters_to_centimeters(millimeters):
    """Convert millimeters to centimeters."""
    return convert(millimeters, 'millimeters', 'centimeters')


def millimeters_to_kilometers(millimeters):
    """Convert millimeters to kilometers."""
    return convert(millimeters, 'millimeters', 'kilometers')


def millimeters_to_inches(millimeters):
    """Convert millimeters to inches."""
    return convert(millimeters, 'millimeters', 'inches')


def millimeters_to_hands(millimeters):
    """Convert millimeters to hands."""
    return convert(millimeters, 'millimeters', 'hands')


def millimeters_to_feet(millimeters):
    """Convert millimeters to feet."""
    return convert(millimeters, 'millimeters', 'feet')


def millimeters_to_yards(millimeters):
    """Convert millimeters to yards."""
    return convert(millimeters, 'millimeters', 'yards')


def millimeters_to_miles(millimeters):
    """Convert millimeters to miles."""
    return convert(millimeters, 'millimeters', 'miles')


def millimeters_to_light_years(millimeters):
    """Convert millimeters to light years."""
    return convert(millimeters, 'millimeters', 'light_years')


def millimeters_to_astronomical_units(millimeters):
    """Convert millimeters to astronomical units."""
    return convert(millimeters, 'millimeters', 'astronomical_units')


def millimeters_to_parsecs(millimeters):
    """Convert millimeters to parsecs."""
    return convert(millimeters, 'millimeters', 'parsecs')


def millimeters_to_nautical_miles(millimeters):
    """Convert millimeters to nautical miles."""
    return convert(millimeters, 'millimeters', 'nautical_miles')


def millimeters_to_angstroms(millimeters):
    """Convert millimeters to angstroms."""
    return convert(millimeters, 'millimeters', 'angstroms')


def millimeters_to_microns(millimeters):
    """Convert millimeters to microns."""
    return convert(millimeters, 'millimeters', 'microns')


def millimeters_to_planck_lengths(millimeters):
    """Convert millimeters to planck lengths."""
    return convert(millimeters, 'millimeters', 'planck_lengths')


def kilometers_to_meters(kilometers):
    """Convert kilometers to meters."""
    return convert(kilometers, 'kilometers', 'meters')


def kilometers_to_centimeters(kilometers):
    """Convert kilometers to centimeters."""
    return convert(kilometers, 'kilometers', 'centimeters')


def kilometers_to_millimeters(kilometers):
    """Convert kilometers to millimeters."""
    return convert(kilometers, 'kilometers', 'millimeters')


def kilometers_to_inches(kilometers):
    """Convert kilometers to inches."""
    return convert(kilometers, 'kilometers', 'inches')


def kilometers_to_hands(kilometers):
    """Convert kilometers to hands."""
    return convert(kilometers, 'kilometers', 'hands')


def kilometers_to_feet(kilometers):
    """Convert kilometers to feet."""
    return convert(kilometers, 'kilometers', 'feet')


def kilometers_to_yards(kilometers):
    """Convert kilometers to yards."""
    return convert(kilometers, 'kilometers', 'yards')


def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""
    return convert(kilometers, 'kilometers', 'miles')


def kilometers_to_light_years(kilometers):
    """Convert kilometers to light years."""
    return convert(kilometers, 'kilometers', 'light_years')


def kilometers_to_astronomical_units(kilometers):
    """Convert kilometers to astronomical units."""
    return convert(kilometers, 'kilometers', 'astronomical_units')


def kilometers_to_parsecs(kilometers):
    """Convert kilometers to parsecs."""
    return convert(kilometers, 'kilometers', 'parsecs')


def kilometers_to_nautical_miles(kilometers):
    """Convert kilometers to nautical miles."""
    return convert(kilometers, 'kilometers', 'nautical_miles')


def kilometers_to_angstroms(kilometers):
    """Convert kilometers to angstroms."""
    return convert(kilometers, 'kilometers', 'angstroms')


def kilometers_to_microns(kilometers):
    """Convert kilometers to microns."""
    return convert(kilometers, 'kilometers', 'microns')


def kilometers_to_planck_lengths(kilometers):
    """Convert kilometers to planck lengths."""
    return convert(kilometers, 'kilometers', 'planck_lengths')


def inches_to_meters(inches):
    """Convert inches to meters."""
    return convert(inches, 'inches', 'meters')


def inches_to_centimeters(inches):
    """Convert inches to centimeters."""
    return convert(inches, 'inches', 'centimeters')


def inches_to_millimeters(inches):
    """Convert inches to millimeters."""
    return convert(inches, 'inches', 'millimeters')


def inches_to_kilometers(inches):
    """Convert inches to kilometers."""
    return convert(inches, 'inches', 'kilometers')


def inches_to_hands(inches):
    """Convert inches to hands."""
    return convert(inches, 'inches', 'hands')


def inches_to_feet(inches):
    """Convert inches to feet."""
    return convert(inches, 'inches', 'feet')


def inches_to_yards(inches):
    """Convert inches to yards."""
    return convert(inches, 'inches', 'yards')


def inches_to_miles(inches):
    """Convert inches to miles."""
    return convert(inches, 'inches', 'miles')


def inches_to_light_years(inches):
    """Convert inches to light years."""
    return convert(inches, 'inches', 'light_years')


def inches_to_astronomical_units(inches):
    """Convert inches to astronomical units."""
    return convert(inches, 'inches', 'astronomical_units')


def inches_to_parsecs(inches):
    """Convert inches to parsecs."""
    return convert(inches, 'inches', 'parsecs')


def inches_to_nautical_miles(inches):
    """Convert inches to nautical miles."""
    return convert(inches, 'inches', 'nautical_miles')


def inches_to_angstroms(inches):
    """Convert inches to angstroms."""
    return convert(inches, 'inches', 'angstroms')


def inches_to_microns(inches):
    """Convert inches to microns."""
    return convert(inches, 'inches', 'microns')


def inches_to_planck_lengths(inches):
    """Convert inches to planck lengths."""
    return convert(inches, 'inches', 'planck_lengths')


def hands_to_meters(hands):
    """Convert hands to meters."""
    return convert(hands, 'hands', 'meters')


def hands_to_centimeters(hands):
    """Convert hands to centimeters."""
    return convert(hands, 'hands', 'centimeters')


def hands_to_millimeters(hands):
    """Convert hands to millimeters."""
    return convert(hands, 'hands', 'millimeters')


def hands_to_kilometers(hands):
    """Convert hands to kilometers."""
    return convert(hands, 'hands', 'kilometers')


def hands_to_inches(hands):
    """Convert hands to inches."""
    return convert(hands, 'hands', 'inches')


def hands_to_feet(hands):
    """Convert hands to feet."""
    return convert(hands, 'hands', 'feet')


def hands_to_yards(hands):
    """Convert hands to yards."""
    return convert(hands, 'hands', 'yards')


def hands_to_miles(hands):
    """Convert hands to miles."""
    return convert(hands, 'hands', 'miles')


def hands_to_light_years(hands):
    """Convert hands to light years."""
    return convert(hands, 'hands', 'light_years')


def hands_to_astronomical_units(hands):
    """Convert hands to astronomical units."""
    return convert(hands, 'hands', 'astronomical_units')


def hands_to_parsecs(hands):
    """Convert hands to parsecs."""
    return convert(hands, 'hands', 'parsecs')


def hands_to_nautical_miles(hands):
    """Convert hands to nautical miles."""
    return convert(hands, 'hands', 'nautical_miles')


def hands_to_angstroms(hands):
    """Convert hands to angstroms."""
    return convert(hands, 'hands', 'angstroms')


def hands_to_microns(hands):
    """Convert hands to microns."""
    return convert(hands, 'hands', 'microns')


def hands_to_planck_lengths(hands):
    """Convert hands to planck lengths."""
    return convert(hands, 'hands', 'planck_lengths')


def feet_to_meters(feet):
    """Convert feet to meters."""
    return convert(feet, 'feet', 'meters')


def feet_to_centimeters(feet):
    """Convert feet to centimeters."""
    return convert(feet, 'feet', 'centimeters')


def feet_to_millimeters(feet):
    """Convert feet to millimeters."""
    return convert(feet, 'feet', 'millimeters')


def feet_to_kilometers(feet):
    """Convert feet to kilometers."""
    return convert(feet, 'feet', 'kilometers')


def feet_to_inches(feet):
    """Convert feet to inches."""
    return convert(feet, 'feet', 'inches')


def feet_to_hands(feet):
    """Convert feet to hands."""
    return convert(feet, 'feet', 'hands')


def feet_to_yards(feet):
    """Convert feet to yards."""
    return convert(feet, 'feet', 'yards')


def feet_to_miles(feet):
    """Convert feet to miles."""
    return convert(feet, 'feet', 'miles')


def feet_to_light_years(feet):
    """Convert feet to light years."""
    return convert(feet, 'feet', 'light_years')


def feet_to_astronomical_units(feet):
    """Convert feet to astronomical units."""
    return convert(feet, 'feet', 'astronomical_units')


def feet_to_parsecs(feet):
    """Convert feet to parsecs."""
    return convert(feet, 'feet', 'parsecs')


def feet_to_nautical_miles(feet):
    """Convert feet to nautical miles."""
    return convert(feet, 'feet', 'nautical_miles')


def feet_to_angstroms(feet):
    """Convert feet to angstroms."""
    return convert(feet, 'feet', 'angstroms')


def feet_to_microns(feet):
    """Convert feet to microns."""
    return convert(feet, 'feet', 'microns')


def feet_to_planck_lengths(feet):
    """Convert feet to planck lengths."""
    return convert(feet, 'feet', 'planck_lengths')


def yards_to_meters(yards):
    """Convert yards to meters."""
    return convert(yards, 'yards', 'meters')


def yards_to_centimeters(yards):
    """Convert yards to centimeters."""
    return convert(yards, 'yards', 'centimeters')


def yards_to_millimeters(yards):
    """Convert yards to millimeters."""
    return convert(yards, 'yards', 'millimeters')


def yards_to_kilometers(yards):
    """Convert yards to kilometers."""
    return convert(yards, 'yards', 'kilometers')


def yards_to_inches(yards):
    """Convert yards to inches."""
    return convert(yards, 'yards', 'inches')


def yards_to_hands(yards):
    """Convert yards to hands."""
    return convert(yards, 'yards', 'hands')


def yards_to_feet(yards):
    """Convert yards to feet."""
    return convert(yards, 'yards', 'feet')


def yards_to_miles(yards):
    """Convert yards to miles."""
    return convert(yards, 'yards', 'miles')


def yards_to_light_years(yards):
    """Convert yards to light years."""
    return convert(yards, 'yards', 'light_years')


def yards_to_astronomical_units(yards):
    """Convert yards to astronomical units."""
    return convert(yards, 'yards', 'astronomical_units')


def yards_to_parsecs(yards):
    """Convert yards to parsecs."""
    return convert(yards, 'yards', 'parsecs')


def yards_to_nautical_miles(yards):
    """Convert yards to nautical miles."""
    return convert(yards, 'yards', 'nautical_miles')


def yards_to_angstroms(yards):
    """Convert yards to angstroms."""
    return convert(yards, 'yards', 'angstroms')


def yards_to_microns(yards):
    """Convert yards to microns."""
    return convert(yards, 'yards', 'microns')


def yards_to_planck_lengths(yards):
    """Convert yards to planck lengths."""
    return convert(yards, 'yards', 'planck_lengths')


def miles_to_meters(miles):
    """Convert miles to meters."""
    return convert(miles, 'miles', 'meters')


def miles_to_centimeters(miles):
    """Convert miles to centimeters."""
    return convert(miles, 'miles', 'centimeters')


def miles_to_millimeters(miles):
    """Convert miles to millimeters."""
    return convert(miles, 'miles', 'millimeters')


def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return convert(miles, 'miles', 'kilometers')


def miles_to_inches(miles):
    """Convert miles to inches."""
    return convert(miles, 'miles', 'inches')


def miles_to_hands(miles):
    """Convert miles to hands."""
    return convert(miles, 'miles', 'hands')


def miles_to_feet(miles):
    """Convert miles to feet."""
    return convert(miles, 'miles', 'feet')


def miles_to_yards(miles):
    """Convert miles to yards."""
    return convert(miles, 'miles', 'yards')


def miles_to_light_years(miles):
    """Convert miles to light years."""
    return convert(miles, 'miles', 'light_years')


def miles_to_astronomical_units(miles):
    """Convert miles to astronomical units."""
    return convert(miles, 'miles', 'astronomical_units')


def miles_to_parsecs(miles):
    """Convert miles to parsecs."""
    return convert(miles, 'miles', 'parsecs')


def miles_to_nautical_miles(miles):
    """Convert miles to nautical miles."""
    return convert(miles, 'miles', 'nautical_miles')


def miles_to_angstroms(miles):
    """Convert miles to angstroms."""
    return convert(miles, 'miles', 'angstroms')


def miles_to_microns(miles):
    """Convert miles to microns."""
    return convert(miles, 'miles', 'microns')


def miles_to_planck_lengths(miles):
    """Convert miles to planck lengths."""
    return convert(miles, 'miles', 'planck_lengths')


def light_years_to_meters(light_years):
    """Convert light years to meters."""
    return convert(light_years, 'light_years', 'meters')


def light_years_to_centimeters(light_years):
    """Convert light years to centimeters."""
    return convert(light_years, 'light_years', 'centimeters')


def light_years_to_millimeters(light_years):
    """Convert light years to millimeters."""
    return convert(light_years, 'light_years', 'millimeters')


def light_years_to_kilometers(light_years):
    """Convert light years to kilometers."""
    return convert(light_years, 'light_years', 'kilometers')


def light_years_to_inches(light_years):
    """Convert light years to inches."""
    return convert(light_years, 'light_years', 'inches')


def light_years_to_hands(light_years):
    """Convert light years to hands."""
    return convert(light_years, 'light_years', 'hands')


def light_years_to_feet(light_years):
    """Convert light years to feet."""
    return convert(light_years, 'light_years', 'feet')


def light_years_to_yards(light_years):
    """Convert light years to yards."""
    return convert(light_years, 'light_years', 'yards')


def light_years_to_miles(light_years):
    """Convert light years to miles."""
    return convert(light_years, 'light_years', 'miles')


def light_years_to_astronomical_units(light_years):
    """Convert light years to astronomical units."""
    return convert(light_years, 'light_years', 'astronomical_units')


def light_years_to_parsecs(light_years):
    """Convert light years to parsecs."""
    return convert(light_years, 'light_years', 'parsecs')


def light_years_to_nautical_miles(light_years):
    """Convert light years to nautical miles."""
    return convert(light_years, 'light_years', 'nautical_miles')


def light_years_to_angstroms(light_years):
    """Convert light years to angstroms."""
    return convert(light_years, 'light_years', 'angstroms')


def light_years_to_microns(light_years):
    """Convert light years to microns."""
    return convert(light_years, 'light_years', 'microns')


def light_years_to_planck_lengths(light_years):
    """Convert light years to planck lengths."""
    return convert(light_years, 'light_years', 'planck_lengths')


def astronomical_units_to_meters(astronomical_units):
    """Convert astronomical units to meters."""
    return convert(astronomical_units, 'astronomical_units', 'meters')


def astronomical_units_to_centimeters(astronomical_units):
    """Convert astronomical units to centimeters."""
    return convert(astronomical_units, 'astronomical_units', 'centimeters')


def astronomical_units_to_millimeters(astronomical_units):
    """Convert astronomical units to millimeters."""
    return convert(astronomical_units, 'astronomical_units', 'millimeters')


def astronomical_units_to_kilometers(astronomical_units):
    """Convert astronomical units to kilometers."""
    return convert(astronomical_units, 'astronomical_units', 'kilometers')


def astronomical_units_to_inches(astronomical_units):
    """Convert astronomical units to inches."""
    return convert(astronomical_units, 'astronomical_units', 'inches')


def astronomical_units_to_hands(astronomical_units):
    """Convert astronomical units to hands."""
    return convert(astronomical_units, 'astronomical_units', 'hands')


def astronomical_units_to_feet(astronomical_units):
    """Convert astronomical units to feet."""
    return convert(astronomical_units, 'astronomical_units', 'feet')


def astronomical_units_to_yards(astronomical_units):
    """Convert astronomical units to yards."""
    return convert(astronomical_units, 'astronomical_units', 'yards')


def astronomical_units_to_miles(astronomical_units):
    """Convert astronomical units to miles."""
    return convert(astronomical_units, 'astronomical_units', 'miles')


def astronomical_units_to_light_years(astronomical_units):
    """Convert astronomical units to light years."""
    return convert(astronomical_units, 'astronomical_units', 'light_years')


def astronomical_units_to_parsecs(astronomical_units):
    """Convert astronomical units to parsecs."""
    return convert(astronomical_units, 'astronomical_units', 'parsecs')


def astronomical_units_to_nautical_miles(astronomical_units):
    """Convert astronomical units to nautical miles."""
    return convert(astronomical_units, 'astronomical_units', 'nautical_miles')


def astronomical_units_to_angstroms(astronomical_units):
    """Convert astronomical units to angstroms."""
    return convert(astronomical_units, 'astronomical_units', 'angstroms')


def astronomical_units_to_microns(astronomical_units):
    """Convert astronomical units to microns."""
    return convert(astronomical_units, 'astronomical_units', 'microns')


def astronomical_units_to_planck_lengths(astronomical_units):
    """Convert astronomical units to planck lengths."""
    return convert(astronomical_units, 'astronomical_units', 'planck_lengths')


def parsecs_to_meters(parsecs):
    """Convert parsecs to meters."""
    return convert(parsecs, 'parsecs', 'meters')


def parsecs_to_centimeters(parsecs):
    """Convert parsecs to centimeters."""
    return convert(parsecs, 'parsecs', 'centimeters')


def parsecs_to_millimeters(parsecs):
    """Convert parsecs to millimeters."""
    return convert(parsecs, 'parsecs', 'millimeters')


def parsecs_to_kilometers(parsecs):
    """Convert parsecs to kilometers."""
    return convert(parsecs, 'parsecs', 'kilometers')


def parsecs_to_inches(parsecs):
    """Convert parsecs to inches."""
    return convert(parsecs, 'parsecs', 'inches')


def parsecs_to_hands(parsecs):
    """Convert parsecs to hands."""
    return convert(parsecs, 'parsecs', 'hands')


def parsecs_to_feet(parsecs):
    """Convert parsecs to feet."""
    return convert(parsecs, 'parsecs', 'feet')


def parsecs_to_yards(parsecs):
    """Convert parsecs to yards."""
    return convert(parsecs, 'parsecs', 'yards')


def parsecs_to_miles(parsecs):
    """Convert parsecs to miles."""
    return convert(parsecs, 'parsecs', 'miles')


def parsecs_to_light_years(parsecs):
    """Convert parsecs to light years."""
    return convert(parsecs, 'parsecs', 'light_years')


def parsecs_to_astronomical_units(parsecs):
    """Convert parsecs to astronomical units."""
    return convert(parsecs, 'parsecs', 'astronomical_units')


def parsecs_to_nautical_miles(parsecs):
    """Convert parsecs to nautical miles."""
    return convert(parsecs, 'parsecs', 'nautical_miles')


def parsecs_to_angstroms(parsecs):
    """Convert parsecs to angstroms."""
    return convert(parsecs, 'parsecs', 'angstroms')


def parsecs_to_microns(parsecs):
    """Convert parsecs to microns."""
    return convert(parsecs, 'parsecs', 'microns')


def parsecs_to_planck_lengths(parsecs):
    """Convert parsecs to planck lengths."""
    return convert(parsecs, 'parsecs', 'planck_lengths')


def nautical_miles_to_meters(nautical_miles):
    """Convert nautical miles to meters."""
    return convert(nautical_miles, 'nautical_miles', 'meters')


def nautical_miles_to_centimeters(nautical_miles):
    """Convert nautical miles to centimeters."""
    return convert(nautical_miles, 'nautical_miles', 'centimeters')


def nautical_miles_to_millimeters(nautical_miles):
    """Convert nautical miles to millimeters."""
    return convert(nautical_miles, 'nautical_miles', 'millimeters')


def nautical_miles_to_kilometers(nautical_miles):
    """Convert nautical miles to kilometers."""
    return convert(nautical_miles, 'nautical_miles', 'kilometers')


def nautical_miles_to_inches(nautical_miles):
    """Convert nautical miles to inches."""
    return convert(nautical_miles, 'nautical_miles', 'inches')


def nautical_miles_to_hands(nautical_miles):
    """Convert nautical miles to hands."""
    return convert(nautical_miles, 'nautical_miles', 'hands')


def nautical_miles_to_feet(nautical_miles):
    """Convert nautical miles to feet."""
    return convert(nautical_miles, 'nautical_miles', 'feet')


def nautical_miles_to_yards(nautical_miles):
    """Convert nautical miles to yards."""
    return convert(nautical_miles, 'nautical_miles', 'yards')


def nautical_miles_to_miles(nautical_miles):
    """Convert nautical miles to miles."""
    return convert(nautical_miles, 'nautical_miles', 'miles')


def nautical_miles_to_light_years(nautical_miles):
    """Convert nautical miles to light years."""
    return convert(nautical_miles, 'nautical_miles', 'light_years')


def nautical_miles_to_astronomical_units(nautical_miles):
    """Convert nautical miles to astronomical units."""
    return convert(nautical_miles, 'nautical_miles', 'astronomical_units')


def nautical_miles_to_parsecs(nautical_miles):
    """Convert nautical miles to parsecs."""
    return convert(nautical_miles, 'nautical_miles', 'parsecs')


def nautical_miles_to_angstroms(nautical_miles):
    """Convert nautical miles to angstroms."""
    return convert(nautical_miles, 'nautical_miles', 'angstroms')


def nautical_miles_to_microns(nautical_miles):
    """Convert nautical miles to microns."""
    return convert(nautical_miles, 'nautical_miles', 'microns')


def nautical_miles_to_planck_lengths(nautical_miles):
    """Convert nautical miles to planck lengths."""
    return convert(nautical_miles, 'nautical_miles', 'planck_lengths')


def angstroms_to_meters(angstroms):
    """Convert angstroms to meters."""
    return convert(angstroms, 'angstroms', 'meters')


def angstroms_to_centimeters(angstroms):
    """Convert angstroms to centimeters."""
    return convert(angstroms, 'angstroms', 'centimeters')


def angstroms_to_millimeters(angstroms):
    """Convert angstroms to millimeters."""
    return convert(angstroms, 'angstroms', 'millimeters')


def angstroms_to_kilometers(angstroms):
    """Convert angstroms to kilometers."""
    return convert(angstroms, 'angstroms', 'kilometers')


def angstroms_to_inches(angstroms):
    """Convert angstroms to inches."""
    return convert(angstroms, 'angstroms', 'inches')


def angstroms_to_hands(angstroms):
    """Convert angstroms to hands."""
    return convert(angstroms, 'angstroms', 'hands')


def angstroms_to_feet(angstroms):
    """Convert angstroms to feet."""
    return convert(angstroms, 'angstroms', 'feet')


def angstroms_to_yards(angstroms):
    """Convert angstroms to yards."""
    return convert(angstroms, 'angstroms', 'yards')


def angstroms_to_miles(angstroms):
    """Convert angstroms to miles."""
    return convert(angstroms, 'angstroms', 'miles')


def angstroms_to_light_years(angstroms):
    """Convert angstroms to light years."""
    return convert(angstroms, 'angstroms', 'light_years')


def angstroms_to_astronomical_units(angstroms):
    """Convert angstroms to astronomical units."""
    return convert(angstroms, 'angstroms', 'astronomical_units')


def angstroms_to_parsecs(angstroms):
    """Convert angstroms to parsecs."""
    return convert(angstroms, 'angstroms', 'parsecs')


def angstroms_to_nautical_miles(angstroms):
    """Convert angstroms to nautical miles."""
    return convert(angstroms, 'angstroms', 'nautical_miles')


def angstroms_to_microns(angstroms):
    """Convert angstroms to microns."""
    return convert(angstroms, 'angstroms', 'microns')


def angstroms_to_planck_lengths(angstroms):
    """Convert angstroms to planck lengths."""
    return convert(angstroms, 'angstroms', 'planck_lengths')


def microns_to_meters(microns):
    """Convert microns to meters."""
    return convert(microns, 'microns', 'meters')


def microns_to_centimeters(microns):
    """Convert microns to centimeters."""
    return convert(microns, 'microns', 'centimeters')


def microns_to_millimeters(microns):
    """Convert microns to millimeters."""
    return convert(microns, 'microns', 'millimeters')


def microns_to_kilometers(microns):
    """Convert microns to kilometers."""
    return convert(microns, 'microns', 'kilometers')


def microns_to_inches(microns):
    """Convert microns to inches."""
    return convert(microns, 'microns', 'inches')


def microns_to_hands(microns):
    """Convert microns to hands."""
    return convert(microns, 'microns', 'hands')


def microns_to_feet(microns):
    """Convert microns to feet."""
    return convert(microns, 'microns', 'feet')


def microns_to_yards(microns):
    """Convert microns to yards."""
    return convert(microns, 'microns', 'yards')


def microns_to_miles(microns):
    """Convert microns to miles."""
    return convert(microns, 'microns', 'miles')


def microns_to_light_years(microns):
    """Convert microns to light years."""
    return convert(microns, 'microns', 'light_years')


def microns_to_astronomical_units(microns):
    """Convert microns to astronomical units."""
    return convert(microns, 'microns', 'astronomical_units')


def microns_to_parsecs(microns):
    """Convert microns to parsecs."""
    return convert(microns, 'microns', 'parsecs')


def microns_to_nautical_miles(microns):
    """Convert microns to nautical miles."""
    return convert(microns, 'microns', 'nautical_miles')


def microns_to_angstroms(microns):
    """Convert microns to angstroms."""
    return convert(microns, 'microns', 'angstroms')


def microns_to_planck_lengths(microns):
    """Convert microns to planck lengths."""
    return convert(microns, 'microns', 'planck_lengths')


def planck_lengths_to_meters(planck_lengths):
    """Convert planck lengths to meters."""
    return convert(planck_lengths, 'planck_lengths', 'meters')


def planck_lengths_to_centimeters(planck_lengths):
    """Convert planck lengths to centimeters."""
    return convert(planck_lengths, 'planck_lengths', 'centimeters')


def planck_lengths_to_millimeters(planck_lengths):
    """Convert planck lengths to millimeters."""
    return convert(planck_lengths, 'planck_lengths', 'millimeters')


def planck_lengths_to_kilometers(planck_lengths):
    """Convert planck lengths to kilometers."""
    return convert(planck_lengths, 'planck_lengths', 'kilometers')


def planck_lengths_to_inches(planck_lengths):
    """Convert planck lengths to inches."""
    return convert(planck_lengths, 'planck_lengths', 'inches')


def planck_lengths_to_hands(planck_lengths):
    """Convert planck lengths to hands."""
    return convert(planck_lengths, 'planck_lengths', 'hands')


def planck_lengths_to_feet(planck_lengths):
    """Convert planck lengths to feet."""
    return convert(planck_lengths, 'planck_lengths', 'feet')


def planck_lengths_to_yards(planck_lengths):
    """Convert planck lengths to yards."""
    return convert(planck_lengths, 'planck_lengths', 'yards')


def planck_lengths_to_miles(planck_lengths):
    """Convert planck lengths to miles."""
    return convert(planck_lengths, 'planck_lengths', 'miles')


def planck_lengths_to_light_years(planck_lengths):
    """Convert planck lengths to light years."""
    return convert(planck_lengths, 'planck_lengths', 'light_years')


def planck_lengths_to_astronomical_units(planck_lengths):
    """Convert planck lengths to astronomical units."""
    return convert(planck_lengths, 'planck_lengths', 'astronomical_units')


def planck_lengths_to_parsecs(planck_lengths):
    """Convert planck lengths to parsecs."""
    return convert(planck_lengths, 'planck_lengths', 'parsecs')


def planck_lengths_to_nautical_miles(planck_lengths):
    """Convert planck lengths to nautical miles."""
    return convert(planck_lengths, 'planck_lengths', 'nautical_miles')


def planck_lengths_to_angstroms(planck_lengths):
    """Convert planck lengths to angstroms."""
    return convert(planck_lengths, 'planck_lengths', 'angstroms')


def planck_lengths_to_microns(planck_lengths):
    """Convert planck lengths to microns."""
    return convert(planck_lengths, 'planck_lengths', 'microns')
