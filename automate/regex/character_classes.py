import re

#  \d+ one or more mumeric
#  \s whitespace character
#  \w+ one or more letter, digit, underscore
xmas_regex = re.compile(r'\d+\s\w+')
print(xmas_regex.findall('12 drummers 11 pipers 10 lords 9 Ladies 8 MAIDS'))

#  define own character class with []
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food self. BABY FOOD'))

#  use ranges of letters or numbers with -
number_range = re.compile(r'[0-5]')
print(number_range.findall('Here are 1 some numbers 9 88 in 3 a range 5.'))

#  Use the ^ just inside the opening [] to get negative characters
consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('Robo Cop eats baby food, BABY FOOD.'))
