print('#' * 10 + ' TUPLES VS. LISTS ' + '#' * 10)
# TUPLES VS. LISTS

# 1. Tuples are faster and more efficient than lists.

# 2. Tuples are safer than lists.

# 3. Tuples can be used as keys in dictionaries.

# 4. Storage efficiency.
import sys
l1 = [1, 2, 3, 4, 5, 6] # LIST
t1 = (1, 2, 3, 4, 5, 6) # TUPLE

print(f'List memory size: {sys.getsizeof(l1)}') # 104
print(f'List memory size: {sys.getsizeof(t1)}') # 96