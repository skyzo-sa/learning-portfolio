print('#' * 10 + ' TRT AND EXCEPT ' + '#' * 10)
#  TRT AND EXCEPT

f = open('hello.txt', 'w+')
try:
    f.write('I love Python')
except:
    print('Cannot write to file!')
else:
    print('File was written successfully!')

finally:
    print('This code is always executed!')
    if not f.closed:
        print(f.read())
        f.close()
    print(f'File closed {f.closed}')


print('#' * 10 + ' NEXT BLOCK OF CODE ' + '#' * 10)