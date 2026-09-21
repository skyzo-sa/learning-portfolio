# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# add a tab to your text \t:
print("Python")
print("\tPython")

# add a new line in a string \n:
print("Languages:\nPython\nC++\nJavaScript")

# combine tabs and newlines in a single string
print("Languages: \n\tPython\n\tC++\n\tJavaScript")

# Stripping Whitespace
favorite_language = "Python "
print(favorite_language.rstrip())

