print('#' * 10 + 'LOGICAL OPERATORS' + '#' * 10)

"""
Logical Operators:
"""

# (and) Returns True if BOTH conditions are True
print(True and True)    # => True
print(True and False)   # => False

age = 25
has_license = True

print(age >= 18 and has_license)  # => True

# (or) Returns True if AT LEAST ONE condition is True
print(True or False)    # => True
print(False or False)   # => False

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)  # => True

# (not) Reverses the Boolean value
print(not True)   # => False
print(not False)  # => True

logged_in = True

print(not logged_in)  # => False

# Combining (and) and (or)
age = 20
has_id = True
is_member = False

# Must be 18 or older AND have an ID
print(age >= 18 and has_id)  # => True


# Can enter if they are a member OR over 18
print(is_member or age >= 18)  # => True


# More complex example
username = "Skyzo"
password_correct = True
account_locked = False

# Login allowed when the password is correct
# AND the account is NOT locked
can_login = password_correct and not account_locked

print(can_login)  # => True