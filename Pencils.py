import random

print('How many pencils would you like to use:')
while True:
    number_of_pencils = input()
    if not number_of_pencils.isdigit():
        print('The number of pencils should be numeric')
    elif int(number_of_pencils) == 0:
        print('The number of pencils should be positive')
    else:
        number_of_pencils = int(number_of_pencils)
        break

print('Who will be the first (John, Jack):')
while True:
    name = input()
    if name in ('John', 'Jack'):
        break
    print("Choose between 'John' and 'Jack'")

while number_of_pencils > 0:

    print('|' * number_of_pencils)
    print(name + "'s turn:")

    while True:
        if name == "Jack":

            if number_of_pencils % 4 == 0:
                n = 3
                print(n)
            elif number_of_pencils % 4 == 3:
                n = 2
                print(n)
            elif number_of_pencils % 4 == 2:
                n = 1
                print(n)
            else:
                n = 1
                print(n)
            break
            
        if name == "John":

            n = input()
            if n not in ('1', '2', '3'):
                print("Possible values: '1', '2' or '3'")
            elif int(n) > number_of_pencils:
                print('Too many pencils were taken')
            else:
                break

    number_of_pencils -= int(n)
    name = 'John' if name == 'Jack' else 'Jack'
else:
    print(name + ' won!')
