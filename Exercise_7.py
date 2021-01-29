def computegrade(a):
    if a < 0 or a > 1:
        return 'Bad score'
    elif a >= 0.9:
        return 'A'
    elif a >= 0.8:
        return 'B'
    elif a >= 0.7:
        return 'C'
    elif a >= 0.6:
        return 'D'
    else:
        return 'E'

try:
    a = float(input('Enter score: '))
    print(computegrade(a))
except:
    print('Bad score')