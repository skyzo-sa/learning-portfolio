print('#' * 10 + 'string_slicing' + '#' * 10)


movie = 'The Godfather'
print(movie[0]) # T

# string_variables[start:stop]
print(movie[2:5]) # => e G
print(movie[:2]) # => Th
print(movie[4:]) # => Godfather
print(movie[-2:]) # => er

# movie[:i] + movie[1:] is equal to movie
print(movie[:4] + movie[4:]) # => The Godfather

# string_variables[start:stop:step]
print(movie[0:10:2]) # => TeGda
print(movie[::]) # => The Godfather
print(movie[::-1]) # => rehtafdoG ehT