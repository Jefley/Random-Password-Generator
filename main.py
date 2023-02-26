from random import choice, randint as ran

numb = '0123456789'
spchar = "?.,><';:/\|][}{=+_-)(*&^%$#@!`~~¿"
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print (' ')
print ('Random password: ')
for t in range(1, ran(8,15)):
    print (choice(alpha+ numb+ spchar), end='')
print ('\n ')

