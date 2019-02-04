# the pipe '|' can match one of may expressions
# if both occur, the first will be returned as a Match object

import re
hero_regex = re.compile(r'Batman|Spider Man')
mo = hero_regex.search('Batman, Spider Man, and Katie')
print(mo.group())
mo2 = hero_regex.search('Spider Man, Katie, and Batman')
print(mo2.group())

# use pipe to match one of several patterns
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
bat_mo = bat_regex.search('The Batcopter wouldn\'t start.')
# bat_mo.group() returns matched text
print(bat_mo.group())
#bat_mo.group(1) returns just the part of match in parens
print(bat_mo.group(1))
