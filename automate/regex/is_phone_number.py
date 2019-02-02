# checks if length is 12
# checks if first 3 characters are numbers
# checks for hyphen
# checks next 3 characters
# checks for hyphen
# checks last 4 characters
# if all pass return True


def isPhoneMumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print('415-555-4242 is a phone number:')
# print(isPhoneMumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneMumber('Moshi moshi'))

message = 'Call me at 415-555-0100 tomorrow. My office number is 415-555-2525'
for i in range(len(message)):
    # iterates through chunks of 12 characters
    chunk = message[i:i+12]
    # if a chunk matches the criteria above
    if isPhoneMumber(chunk):
        print(f'Phone number found: {chunk}')
print('DONE')
