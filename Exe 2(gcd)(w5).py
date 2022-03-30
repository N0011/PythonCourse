while True:
    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))

    if (num1 < 1 or num2 < 1):
        print('The program is terminated.')
        break

    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp

    while (num2 != 0):
        r = num1 % num2
        num1 = num2
        num2 = r

    print('gcd(num1,num2) = ', num1,)
