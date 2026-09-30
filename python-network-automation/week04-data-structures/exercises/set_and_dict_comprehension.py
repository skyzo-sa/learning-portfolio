print('#' * 10 + ' SET AND DICTIONARY COMPREHENSIONS ' + '#' * 10)
# SET AND DICTIONARY COMPREHENSIONS

#1. # SET COMPREHENSION
names = {'tom', 'ANNE', 'JaMes', 'dAn', 'guGU'}
names = {n.capitalize() for n in names}
print(names) # {'Dan', 'James', 'Gugu', 'Tom', 'Anne'}

#2. DICTIONARY COMPREHENSION
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {k*2: v*2 for k, v in d1.items()}
print(d2) # {'aa': 2, 'bb': 4, 'cc': 6}

d3 = {k.upper(): v*2 for k, v in d1.items() if v % 3 == 0}
print(d3)  # {'C': 6}

#3. zip() function
years = [2017, 2018, 2019]
revenues = [30000, 40000, 50000]
z = zip(years, revenues)
sales = list(z)
print(sales)

my_sales = dict(zip(years, revenues))
print(my_sales) # {2017: 30000, 2018: 40000, 2019: 50000}

profit = {k: v*0.15 for k,v in my_sales.items()}
print(profit) # {2017: 4500.0, 2018: 6000.0, 2019: 7500.0}