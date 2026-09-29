print('#' * 10 + ' SETS METHODS - PAR 2 ' + '#' * 10)
# union(), intersections(), difference(), symmetric difference()

set1 = {1, 3, 5}
set2 = {5, 7, 9}

#1. set.intersections() &
set3 = set1.intersection(set2)
print(f'set3: {set3}') # {5}

set3 = set1 & set2
print(f'set3: {set3}') # {5}

#2. set.difference() -
set4 = set1.difference(set2)
print(f'set4: {set4}')  # {1, 3}

set4 = set1 - set2
print(f'set4: {set4}') # # {1, 3}

#3. set.symmetric difference() ^
set5 = set1.symmetric_difference(set2)
print(f'set5: {set5}') # {1, 3, 7, 9}

set5 = set1 ^ set2
print(f'set5: {set5}') # {1, 3, 7, 9}

#4. set.union() |
set6 = set1.union(set2)
print(f'set6: {set6}') # {1, 3, 5, 7, 9}

set6 = set1 | set2
print(f'set6: {set6}')  # {1, 3, 5, 7, 9}

#5. set.isdisjoin()
s1 = {1, 3, 5}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2)) # False
s3 = {8, 9}
print(s1.isdisjoint(s3)) # True

"""
< lesser than, 
<= lesser than or equal to, 
> greater than, 
>= greater than or equal to
"""
print({1, 3} < {1, 2, 3, 4}) # True
print({1, 3} > {1, 2, 3, 4}) # False



