import re

# \d means digit character
# the r marks the string as raw string so escapes aren't needed
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# the search() method searches string for regex match
# if pattern is found, search() returns a Match object
mo = phone_number_regex.search('My number is 415-555-2543.')
# Match objects have a group() method that will return the actual match
print(f'The phone number found is: {mo.group()}')

ssn = re.compile(r'\d\d\d-\d\d-\d\d\d\d')
my_ssn = ssn.search("You'll never get 000-00-0000 my SSN!")
print(f'Found SSN: {my_ssn.group()}')
