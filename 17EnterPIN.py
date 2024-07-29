print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1100:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1100:
  print('PIN accepted!')