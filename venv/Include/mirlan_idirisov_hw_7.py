from random import randint
import datetime

c = 1
a = randint(1, 100)
start = datetime.datetime.now()

while True:
    b = input('enter number from 1 to 100: ')
    try:
        if 1 < int(b) < 100:
            if int(b) > a:
                print('<')
                c += 1
            elif int(b) < a:
                print('>')
                c +=1
            elif int(b) == a:
                print('\nYou won!')
                break
        else:
            print('enter number only from 1 to 100')
    except ValueError:
        print('enter number, not value or letter')
print(f'\nYou used {c} guesses')
print(f'You spent {datetime.datetime.now() - start} seconds\n')