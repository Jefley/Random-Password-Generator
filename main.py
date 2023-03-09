from random import choice, randint as ran
from time import sleep

numb = '0123456789'
spchar = "?.,><';:/\|][}{=+_-)(*&^%$#@!`~~¿"
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print (' ')
print ('Random password: ')
while True:
    for t in range(1, ran(10,15)):
        print (choice(alpha+ numb+ spchar), end='')
    print ('\n ')
    sleep(1)
    quest = str(input('Get new results? [Y/N]: ')).upper()
    while quest not in 'YN':
        print(' ')
        sleep(1)
        quest = input('invalid answer, get new results? [Y/N] ').upper()
    if quest == 'N':
        print('Program was finished')
        print(' ')
        sleep(1)
        break
