import re

# use parens to group
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-1234')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())  # notice the plural
# mo.groups() returns a tuple
# use the multiple assignment trick to assign variables
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# if you are searching for text with parens
# need to escape. Ex is area code in parens
parenRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
moMo = parenRegex.search('My phone number is (415) 555-2134.')
print(moMo.group(1))
print(moMo.group(2))

socRegex = re.compile(r'(\d\d\d)-(\d\d)-(\d\d\d\d)')
socSearch = socRegex.search('My social is 000-25-0000')
firstGroup, secGroup, thirGroup = socSearch.groups()
print(secGroup)
# trying something git
