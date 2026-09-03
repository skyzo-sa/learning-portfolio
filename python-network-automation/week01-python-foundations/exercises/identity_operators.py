"""
Identity Operators:
"""

"""
Mutability vs Immutability:

The value of mutable variable can be changed after it has been created,
but the value of an immutable variable cannot be changed.

Immutable types: int, float, str, tuple, frozenset

Mutable types: list, set, dict
"""

a, b = 3, 4
# ("is")
print(a is b) # returns => False

print(id(a)) # Original ID 140734969173176
a += 3
print(a) # => 6
print(id(a)) # Changed ID 140734969173272

# list
numbers = [1, 2, 3]
print(id(numbers))
numbers.append(100)
print(numbers) # => [1, 2, 3, 100]

nums = numbers.copy()
print(nums == numbers) # => True
print(nums) # => [1, 2, 3, 100]
print(nums is numbers)  # # => False

# ("is not")
