# INDEXING STRINGS
"""
A string is ordered sequence of UTF-8 encoded characters

i.e
my_str = 'Python'
index: 0 1 3 2 4 5
"""
movie = "The Godfather"
# index: 0 1 3 2 4 5 6 7 8 9 10 11 12

print(movie[0]) # => returns "T"
print(movie[3]) # => returns "blank"
print(movie[4]) # => returns "G"
print(movie[-1]) # => returns "r" last value
print(movie[-3]) # => returns "h" 3rd valued before last.

# print('Python'[7]) # IndexError: string index out of range
print('Python'[4]) # => returns "o"
print(len('Python')) # => returns "6"

s1 = 'I love Python programming!'
print(len(s1)) # => 26 characters
print(s1[-3]) # # => "n" character

n = len(s1)
print(s1[n-1]) #  => "!" character

print(s1[0])
# TypeError: 'str' object does not support item assignment
s1[0] = 'X'
print(s1[0])



