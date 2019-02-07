import re

#  The * means search for zero or more instances
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The adventures of Batman')
mo2 = bat_regex.search('The adventures of Batwoman')
mo3 = bat_regex.search('The adventures of Batwowowowowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())
