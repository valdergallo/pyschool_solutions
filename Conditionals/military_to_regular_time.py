"""
Write a function that converts the time from military to regular format.

Examples

>>> time12hr('1619')
'4:19 p.m.'
>>> time12hr('1200')
'12:00 p.m.'
>>> time12hr('1020')
'10:20 a.m.'
"""


def time12hr(tmstr):
    from datetime import datetime
    instance = datetime.strptime(tmstr, '%H%M')
    tmstr = instance.strftime('%I:%M %p')

    tmstr = tmstr.replace('AM', 'a.m.').replace('PM', 'p.m.')
    if tmstr[0] == '0':
        tmstr = tmstr[1:]

    return tmstr
