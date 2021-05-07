from .converter import convert

""" The code in this file was created from this code:
s = '''
def {{a}}_to_{{b}}({{a}}):
    return convert({{a}}, '{{a}}', '{{b}}')'''

# these time units (with 'second' added) were taken from:
# https://github.com/hgrecco/pint/blob/ffc05dcf92347b217e14adbf96c36160f6128627/pint/default_en.txt#L168
l = ['second',
'minute',
'hour',
'day',
'week',
'fortnight',
'year',
'month',
'century',
'millennium',]
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

file_append('../democritus_core/time_converter.py', '\n\n\n'.join(funcs))
"""


def seconds_to_minutes(seconds):
    """Convert seconds to minutes."""
    return convert(seconds, 'seconds', 'minutes')


def seconds_to_hours(seconds):
    """Convert seconds to hours."""
    return convert(seconds, 'seconds', 'hours')


def seconds_to_days(seconds):
    """Convert seconds to days."""
    return convert(seconds, 'seconds', 'days')


def seconds_to_weeks(seconds):
    """Convert seconds to weeks."""
    return convert(seconds, 'seconds', 'weeks')


def seconds_to_fortnights(seconds):
    """Convert seconds to fortnights."""
    return convert(seconds, 'seconds', 'fortnights')


def seconds_to_years(seconds):
    """Convert seconds to years."""
    return convert(seconds, 'seconds', 'years')


def seconds_to_months(seconds):
    """Convert seconds to months."""
    return convert(seconds, 'seconds', 'months')


def seconds_to_centuries(seconds):
    """Convert seconds to centuries."""
    return convert(seconds, 'seconds', 'centuries')


def seconds_to_millenniums(seconds):
    """Convert seconds to millenniums."""
    return convert(seconds, 'seconds', 'millenniums')


def minutes_to_seconds(minutes):
    """Convert minutes to seconds."""
    return convert(minutes, 'minutes', 'seconds')


def minutes_to_hours(minutes):
    """Convert minutes to hours."""
    return convert(minutes, 'minutes', 'hours')


def minutes_to_days(minutes):
    """Convert minutes to days."""
    return convert(minutes, 'minutes', 'days')


def minutes_to_weeks(minutes):
    """Convert minutes to weeks."""
    return convert(minutes, 'minutes', 'weeks')


def minutes_to_fortnights(minutes):
    """Convert minutes to fortnights."""
    return convert(minutes, 'minutes', 'fortnights')


def minutes_to_years(minutes):
    """Convert minutes to years."""
    return convert(minutes, 'minutes', 'years')


def minutes_to_months(minutes):
    """Convert minutes to months."""
    return convert(minutes, 'minutes', 'months')


def minutes_to_centuries(minutes):
    """Convert minutes to centuries."""
    return convert(minutes, 'minutes', 'centuries')


def minutes_to_millenniums(minutes):
    """Convert minutes to millenniums."""
    return convert(minutes, 'minutes', 'millenniums')


def hours_to_seconds(hours):
    """Convert hours to seconds."""
    return convert(hours, 'hours', 'seconds')


def hours_to_minutes(hours):
    """Convert hours to minutes."""
    return convert(hours, 'hours', 'minutes')


def hours_to_days(hours):
    """Convert hours to days."""
    return convert(hours, 'hours', 'days')


def hours_to_weeks(hours):
    """Convert hours to weeks."""
    return convert(hours, 'hours', 'weeks')


def hours_to_fortnights(hours):
    """Convert hours to fortnights."""
    return convert(hours, 'hours', 'fortnights')


def hours_to_years(hours):
    """Convert hours to years."""
    return convert(hours, 'hours', 'years')


def hours_to_months(hours):
    """Convert hours to months."""
    return convert(hours, 'hours', 'months')


def hours_to_centuries(hours):
    """Convert hours to centuries."""
    return convert(hours, 'hours', 'centuries')


def hours_to_millenniums(hours):
    """Convert hours to millenniums."""
    return convert(hours, 'hours', 'millenniums')


def days_to_seconds(days):
    """Convert days to seconds."""
    return convert(days, 'days', 'seconds')


def days_to_minutes(days):
    """Convert days to minutes."""
    return convert(days, 'days', 'minutes')


def days_to_hours(days):
    """Convert days to hours."""
    return convert(days, 'days', 'hours')


def days_to_weeks(days):
    """Convert days to weeks."""
    return convert(days, 'days', 'weeks')


def days_to_fortnights(days):
    """Convert days to fortnights."""
    return convert(days, 'days', 'fortnights')


def days_to_years(days):
    """Convert days to years."""
    return convert(days, 'days', 'years')


def days_to_months(days):
    """Convert days to months."""
    return convert(days, 'days', 'months')


def days_to_centuries(days):
    """Convert days to centuries."""
    return convert(days, 'days', 'centuries')


def days_to_millenniums(days):
    """Convert days to millenniums."""
    return convert(days, 'days', 'millenniums')


def weeks_to_seconds(weeks):
    """Convert weeks to seconds."""
    return convert(weeks, 'weeks', 'seconds')


def weeks_to_minutes(weeks):
    """Convert weeks to minutes."""
    return convert(weeks, 'weeks', 'minutes')


def weeks_to_hours(weeks):
    """Convert weeks to hours."""
    return convert(weeks, 'weeks', 'hours')


def weeks_to_days(weeks):
    """Convert weeks to days."""
    return convert(weeks, 'weeks', 'days')


def weeks_to_fortnights(weeks):
    """Convert weeks to fortnights."""
    return convert(weeks, 'weeks', 'fortnights')


def weeks_to_years(weeks):
    """Convert weeks to years."""
    return convert(weeks, 'weeks', 'years')


def weeks_to_months(weeks):
    """Convert weeks to months."""
    return convert(weeks, 'weeks', 'months')


def weeks_to_centuries(weeks):
    """Convert weeks to centuries."""
    return convert(weeks, 'weeks', 'centuries')


def weeks_to_millenniums(weeks):
    """Convert weeks to millenniums."""
    return convert(weeks, 'weeks', 'millenniums')


def fortnights_to_seconds(fortnights):
    """Convert fortnights to seconds."""
    return convert(fortnights, 'fortnights', 'seconds')


def fortnights_to_minutes(fortnights):
    """Convert fortnights to minutes."""
    return convert(fortnights, 'fortnights', 'minutes')


def fortnights_to_hours(fortnights):
    """Convert fortnights to hours."""
    return convert(fortnights, 'fortnights', 'hours')


def fortnights_to_days(fortnights):
    """Convert fortnights to days."""
    return convert(fortnights, 'fortnights', 'days')


def fortnights_to_weeks(fortnights):
    """Convert fortnights to weeks."""
    return convert(fortnights, 'fortnights', 'weeks')


def fortnights_to_years(fortnights):
    """Convert fortnights to years."""
    return convert(fortnights, 'fortnights', 'years')


def fortnights_to_months(fortnights):
    """Convert fortnights to months."""
    return convert(fortnights, 'fortnights', 'months')


def fortnights_to_centuries(fortnights):
    """Convert fortnights to centuries."""
    return convert(fortnights, 'fortnights', 'centuries')


def fortnights_to_millenniums(fortnights):
    """Convert fortnights to millenniums."""
    return convert(fortnights, 'fortnights', 'millenniums')


def years_to_seconds(years):
    """Convert years to seconds."""
    return convert(years, 'years', 'seconds')


def years_to_minutes(years):
    """Convert years to minutes."""
    return convert(years, 'years', 'minutes')


def years_to_hours(years):
    """Convert years to hours."""
    return convert(years, 'years', 'hours')


def years_to_days(years):
    """Convert years to days."""
    return convert(years, 'years', 'days')


def years_to_weeks(years):
    """Convert years to weeks."""
    return convert(years, 'years', 'weeks')


def years_to_fortnights(years):
    """Convert years to fortnights."""
    return convert(years, 'years', 'fortnights')


def years_to_months(years):
    """Convert years to months."""
    return convert(years, 'years', 'months')


def years_to_centuries(years):
    """Convert years to centuries."""
    return convert(years, 'years', 'centuries')


def years_to_millenniums(years):
    """Convert years to millenniums."""
    return convert(years, 'years', 'millenniums')


def months_to_seconds(months):
    """Convert months to seconds."""
    return convert(months, 'months', 'seconds')


def months_to_minutes(months):
    """Convert months to minutes."""
    return convert(months, 'months', 'minutes')


def months_to_hours(months):
    """Convert months to hours."""
    return convert(months, 'months', 'hours')


def months_to_days(months):
    """Convert months to days."""
    return convert(months, 'months', 'days')


def months_to_weeks(months):
    """Convert months to weeks."""
    return convert(months, 'months', 'weeks')


def months_to_fortnights(months):
    """Convert months to fortnights."""
    return convert(months, 'months', 'fortnights')


def months_to_years(months):
    """Convert months to years."""
    return convert(months, 'months', 'years')


def months_to_centuries(months):
    """Convert months to centuries."""
    return convert(months, 'months', 'centuries')


def months_to_millenniums(months):
    """Convert months to millenniums."""
    return convert(months, 'months', 'millenniums')


def centuries_to_seconds(centuries):
    """Convert centuries to seconds."""
    return convert(centuries, 'centuries', 'seconds')


def centuries_to_minutes(centuries):
    """Convert centuries to minutes."""
    return convert(centuries, 'centuries', 'minutes')


def centuries_to_hours(centuries):
    """Convert centuries to hours."""
    return convert(centuries, 'centuries', 'hours')


def centuries_to_days(centuries):
    """Convert centuries to days."""
    return convert(centuries, 'centuries', 'days')


def centuries_to_weeks(centuries):
    """Convert centuries to weeks."""
    return convert(centuries, 'centuries', 'weeks')


def centuries_to_fortnights(centuries):
    """Convert centuries to fortnights."""
    return convert(centuries, 'centuries', 'fortnights')


def centuries_to_years(centuries):
    """Convert centuries to years."""
    return convert(centuries, 'centuries', 'years')


def centuries_to_months(centuries):
    """Convert centuries to months."""
    return convert(centuries, 'centuries', 'months')


def centuries_to_millenniums(centuries):
    """Convert centuries to millenniums."""
    return convert(centuries, 'centuries', 'millenniums')


def millenniums_to_seconds(millenniums):
    """Convert millenniums to seconds."""
    return convert(millenniums, 'millenniums', 'seconds')


def millenniums_to_minutes(millenniums):
    """Convert millenniums to minutes."""
    return convert(millenniums, 'millenniums', 'minutes')


def millenniums_to_hours(millenniums):
    """Convert millenniums to hours."""
    return convert(millenniums, 'millenniums', 'hours')


def millenniums_to_days(millenniums):
    """Convert millenniums to days."""
    return convert(millenniums, 'millenniums', 'days')


def millenniums_to_weeks(millenniums):
    """Convert millenniums to weeks."""
    return convert(millenniums, 'millenniums', 'weeks')


def millenniums_to_fortnights(millenniums):
    """Convert millenniums to fortnights."""
    return convert(millenniums, 'millenniums', 'fortnights')


def millenniums_to_years(millenniums):
    """Convert millenniums to years."""
    return convert(millenniums, 'millenniums', 'years')


def millenniums_to_months(millenniums):
    """Convert millenniums to months."""
    return convert(millenniums, 'millenniums', 'months')


def millenniums_to_centuries(millenniums):
    """Convert millenniums to centuries."""
    return convert(millenniums, 'millenniums', 'centuries')
