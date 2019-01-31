# Caeser Cipher algorithm problem from Free Code Camp
# done in Python. Because Python Love!!
# With a twist.....input from user

# chr() converts number to letter
char = chr(65 + 1)
print(char)

# ord() converts letter to number
number = ord("A")
print(number)

cipher = input('Please enter your phrase here: ')
cipher = cipher.upper()


def rot13(string):
    solved = ""
    for i in range(len(string)):
        ascii_number = ord(string[i])
        if ascii_number >= 65 and ascii_number <= 77:
            solved += chr(ascii_number + 13)
        elif ascii_number >= 78 and ascii_number <= 90:
            solved += chr(ascii_number - 13)
        else:
            solved += string[i]
    return solved


print(rot13(cipher))
