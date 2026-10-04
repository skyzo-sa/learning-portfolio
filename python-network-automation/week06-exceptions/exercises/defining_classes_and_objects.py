print('#' * 10 + ' OOP : DEFINING CLASSES AND OBJECTS ' + '#' * 10)
# OOP : DEFINING CLASSES AND OBJECTS

class Robot:
    """ This class implements a robot """
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __del__(self):
        print('Robot destroyed!')

    def setEnergy(self, energy):
        self.energy = energy

r1 = Robot('R1', 2026)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(f'Robot year: {r1.year}')
r1.setEnergy(500)
print(r1.energy) # 500
print(getattr(r1, 'energy')) # 500

print(r1.__dict__)