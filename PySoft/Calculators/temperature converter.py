converter = True
while converter:
    print('Celsius and Fahrenheit Converter')
    print('==============================================')
    print('1 -> Celsius > Fahrenheit.')
    print('2 -> Fahrenheit > Celsius.')
    print('3 -> Celsius > Kelvin.')
    print('4 -> Kelvin > Celsius.')
    print('5 -> Fahrenheit > Kelvin.')
    print('6 -> Kelvin > Fahrenheit.')
    option = int(input("Select option: "))
    if option == 1:
        print()
        celsius1 = float(input('Enter a temperature in Celsius: '))
        fahrenheit1 = (celsius1 * 9 / 5) + 32
        print(celsius1,'degrees Celsius is',fahrenheit1,'degrees Fahrenheit.')
    elif option == 2:
        print()
        fahrenheit2 = float(input('Enter a temperature in Fahrenheit: '))
        celsius2 = (fahrenheit2 - 32) * 5 / 9
        print(fahrenheit2,'degrees Fahrenheit is',celsius2,'degrees Celsius.')
    elif option == 3:
        print()
        celsius3 = float(input('Enter a temperature in Celsius: '))
        kelvin3 = celsius3 + 273.15
        print(celsius3,'degrees Celsius is',kelvin3,'degrees Kelvin.')
    elif option == 4:
        print()
        kelvin4 = float(input('Enter a temperature in Kelvin: '))
        celsius4 = kelvin4 - 273.15
        print(celsius3,'degrees Kelvin is',kelvin3,'degrees Celsius.')
    elif option == 5:
        print()
        fahrenheit5 = float(input('Enter a temperature in Fahrenheit: '))
        kelvin5 = (fahrenheit5 - 32) * 5 / 9 + 273.15
        print(fahrenheit5,'degrees Fahrenheit is',kelvin5,'degrees Kelvin.')
    elif option == 6:
        print()
        kelvin6 = float(input('Enter a temperature in Kelvin: '))
        fahrenheit6 = kelvin6 - 273.15 * 9/5 + 32
        print(kelvin6,'degrees Kelvin is',fahrenheit6,'degrees Fahrenheit.')
