# STRING CONCATENATION AND REPETITION
print('#' * 10 + 'string_concatenation_and_repetition' + '#' * 10)

# + => the concatenating operator

movie = 'The Godfather'
director = 'Francis Ford Coppola'
movie_and_director = movie + director
print(movie_and_director)
print(movie + ' was directed by ' + director)

print('abc' '123')
language = 'Python '
version = 3.14

# TypeError: can only concatenate str (not "float") to str
# print(language + version)

print(language + str(version))

# * => the repetition operator

print(movie * 5)
print('#' * 50)

price = '10.5'
print(price * 5)

print(float(price) * 5)

