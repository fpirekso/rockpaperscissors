import time
import random

print('I am rock, paper, scissors Bot!')
time.sleep(0.7)
user = input('What do you choose? ')
time.sleep(0.7)
print('Rock!')
time.sleep(0.7)
print('Paper!')
time.sleep(0.7)
print('Scissors!')
time.sleep(0.7)
print('Say Shoot!')


comp = random.randint(1,4)

if comp == 1:
	comp = 'Rock'
	time.sleep(0.7)
	print('Rock')
elif comp == 2:
	comp = 'Paper'
	time.sleep(0.7)
	print('Paper')
elif comp == 3:
	comp = 'Gun'
	time.sleep(0.7)
	print('Gun')
else:
	comp = 'Scissors'
	time.sleep(0.7)
	print('Scissors')

if user == 'Rock' and comp == 'Rock':
	print('Go again')
elif user == 'Rock' and comp == 'Paper':
	print('You Lost sorry.')
elif user == 'Rock' and comp == 'Scissors':
	print('You Won!')
elif user == 'Paper' and comp == 'Paper':
	print('Go again.')
elif user == 'Paper' and comp == 'Rock':
	print('You Won!')
elif user == 'Paper' and comp == 'Scissors':
	print('You Lost sorry.')
elif user == 'Scissors' and comp == 'Paper':
	print('You Won!')
elif user == 'Scissors' and comp == 'Rock':
	print('You Lost sorry.')
elif user == 'rock' and comp == 'Rock':
	print('Go again')
elif user == 'rock' and comp == 'Paper':
	print('You Lost sorry.')
elif user == 'rock' and comp == 'Scissors':
	print('You Won!')
elif user == 'paper' and comp == 'Paper':
	print('Go again.')
elif user == 'paper' and comp == 'Rock':
	print('You Won!')
elif user == 'paper' and comp == 'Scissors':
	print('You Lost sorry.')
elif user == 'scissors' and comp == 'Paper':
	print('You Won!')
elif user == 'scissors' and comp == 'Rock':
	print('You Lost sorry.')
elif user == 'scissors' and comp == 'Scissors':
	print('Go again')
elif user == 'Scissors' and comp == 'Gun':
	print('You Lost sorry.')
elif user == 'Rock' and comp == 'Gun':
	print('You Lost sorry.')
elif user == 'Paper' and comp == 'Gun':
	print('You Lost sorry.')
elif user == 'scissors' and comp == 'Gun':
	print('You Lost sorry.')
elif user == 'rock' and comp == 'Gun':
	print('You Lost sorry.')
elif user == 'paper' and comp == 'Gun':
	print('You Lost sorry.')
else:
	print('Go again')


