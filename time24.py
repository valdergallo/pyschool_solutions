"""
Write a function that converts the time to 24hr format.

>>> time24hr('12:34am')
'0034hr'
>>> time24hr('12:15pm')
'1215hr'
>>> time24hr('7:28pm')
'1928hr'
>>> time24hr('1:28pm')
'1328hr'

"""


def time24hr(tstr):
    hour, minut = tstr.split(':')
    hour = int(hour)

    if 'pm' in minut and hour == 12:
        hour = 0

    hour = (hour + 12 < 23) and (hour + 12) or (hour - 12)

    minut = minut.replace('am', 'hr')
    minut = minut.replace('pm', 'hr')

    return '%02d%s' % (hour, minut)
