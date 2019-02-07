import re

#  Using the + means match one or more
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The adventures of Batwoman')
mo2 = bat_regex.search('The adventures of Batwowowowowowowoman')
mo3 = bat_regex.search('The adventures of Batman')
print(mo1.group())
print(mo2.group())
#  I'm throwing an error
#  'NoneType' object has no attribute 'group'
print(mo3.group())
