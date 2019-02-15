import re

phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search('Cell: 455-555-1234 Work: 455-555-4321')
print(mo.group())

#  no groups returns a list of strings
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(phone_regex.findall('Cell: 455-555-1234 Work: 455-555-4321'))

#  # groups returns a list of tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall('Cell: 455-555-1234 Work: 455-555-4321'))
