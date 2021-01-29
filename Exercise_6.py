def computepay(hours, rate):
    if a <= 40:
        return a * b
    else:
        return 40 * b + (a - 40) * b * 1.5

try:
    a = float(input('Enter Hours: '))
    b = float(input('Enter Rate: '))
    print('Pay: ', computepay(a, b))
except:
    print('Error, please enter numeric input')