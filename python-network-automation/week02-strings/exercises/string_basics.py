# INTRO TO PYTHON STRINGS
print('#' * 10 + ' STRING BASICS ' + '#' * 10)


name = "ada lovelace"
print(name.title())

my_str1 = 'I learn Python.'
my_str2 = "I learn Python."
print(my_str1)
print(my_str2)

# Hi there! I'm Skyzo.
# SyntaxError: unterminated string literal
print('Hi there! I\'m Skyzo')
print("Hi there! I'm Skyzo")

# class 'str'
message = 'He said: "Got for it!"'
print(message)
print(type(message))

# Multi line strings
languages = """I like Python,
Golang
and 
Solidity.
"""
print(languages)

my_languages = 'I like Python,\nGolang,\nand Solidity.'
print(my_languages)

print('a\tb\tc\td\ne')

print('\\n')

print('He says: "I\'m 20"')
print('\\ is a special character in Python.')
