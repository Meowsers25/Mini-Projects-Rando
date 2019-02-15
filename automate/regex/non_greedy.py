import re

greedy_ha = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha.search('HaHaHaHaHa')
print(mo1.group())
#  The ? after the {} does a non-greedy search(lower number)
non_greedy_ha = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha.search('HaHaHaHaHa')
print(mo2.group())
