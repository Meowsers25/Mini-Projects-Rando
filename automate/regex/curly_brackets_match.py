import re

#  Use {} to search number of instances
#  Can search range {3,5}
#  Or {,5} {3,} up to 5 / 3 or more
ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHa')
print(mo1.group())
mo2 = ha_regex.search('Ha')
#  Same NoneType error
# print(mo2.group())
