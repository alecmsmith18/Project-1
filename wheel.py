pocket_number = int(input('Enter Pocket Number: '))
if pocket_number < 0 or pocket_number > 36:
    print('Invalid Number')
else:
    if pocket_number == 0:
        print('Pocket', pocket_number, 'is Green')
    elif (0 < pocket_number <= 10 and pocket_number % 2 == 1) or \
            (11 < pocket_number <= 18 and pocket_number % 2 == 0) or \
            (19 < pocket_number <= 28 and pocket_number % 2 == 1) or \
            (29 < pocket_number <= 36 and pocket_number % 2 == 0):
        print('Pocket', pocket_number, 'is Red')
    else:
        print('Pocket', pocket_number, 'is Black')



