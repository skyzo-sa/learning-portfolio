# CONVERTING TYPES

# # i mile =  1.609 km
#
# miles = float(input('Enter distance in miles: '))
# # class 'str'
# # print (type(miles))
#
# # TypeError: can't multiply sequence by non-int
# km = miles * 1.609
# #miles = float(miles)
# print('Distance in kilometers:', km)


a = 10 # int
b = 2.5 #float
c = '8.2' #str

# int => float
a_float = float(a)
print('a:', type(a)) # class 'int'
print('a_float:', type(a_float)) # class 'float'

# float => int
b_int = int(b)
print('b:', type(b)) # class 'float'
print('b_int:', type(b_int)) # class 'int'

# float => str
b_str = str(b)
print('b_str:', type(b_str)) # class 'str'

# str => float
c_float = float(c)
print('c_float:', type(c_float)) # class 'float'

# str => int

# ValueError: invalid literal for int()
# c_int = int(c)

c_int = int(float(c))
print('c_int:', type(c_int)) # class 'int'







