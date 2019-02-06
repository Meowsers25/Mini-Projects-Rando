import re
# the (wo)? means that that pattern is optional
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The adventurs ot Batwoman')
print(mo2.group())

#  this example makes area codes optional
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phone1 = phone_regex.search('My number is 555-000-1234')
print(phone1.group())
phone2 = phone_regex.search('My number is 000-1234')
print(phone2.group())
