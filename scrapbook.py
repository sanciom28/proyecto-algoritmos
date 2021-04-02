class Father:
    print('executing father class')

class Son(Father):
    print('executing son class')

matteo = Son()
print(type(matteo))

for i in range(0,10):
    print('a')