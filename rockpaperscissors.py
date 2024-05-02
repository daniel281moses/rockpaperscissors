import random

age = input('What is your age: ')
age = int(age)
if age < 18:
    print ('You are too small to gamble (under 18) - go to school tzootzik!')
    exit()

print('Let\'s Play, the first one who wins 3 times take all the money.')

money = 0
while (money < 50):
    money = input ('How mach money you bet? ')
    money = int(money)
    if money >= 50:
        print ('Let\'s play!') 
    if money < 50: 
        print ('My minimum bet is 50, what\'s your bet? ')

man_score = 0 
computer_score = 0

while (man_score < 3 and computer_score < 3):
    computer_rand_number  = random.randint(1, 3)
    if computer_rand_number == 1:
        computer = 'stone' 
    if computer_rand_number == 2:
        computer = 'paper'
    if computer_rand_number == 3:
        computer = 'scissors'

    print ("I chose stone paper or scissors but I'm going to tell you only after you will choose one")
    man = input('What do you choose? stone paper or scissors? ')
    print ("I chose: " + computer + "!")

    if man == 'stone'and computer == 'stone':
        print('Tie - nobody get\'s a point.')
    if man == 'stone'and computer == 'scissors':
        print('You won, you get a point.')
        man_score += 1
    if man == 'stone'and computer == 'paper':
        print('I won, I get a point.')
        computer_score += 1
        
    if man == 'paper'and computer == 'paper':
        print('Tie - nobody get\'s a point.')
    if man == 'paper'and computer == 'stone':
        print('You won, you get a point.')
        man_score += 1
    if man == 'paper'and computer == 'scissors':
        print('I won, I get a point.')
        computer_score += 1

    if man == 'scissors'and computer == 'scissors':
        print('Tie - nobody get\'s a point.')
    if man == 'scissors'and computer == 'paper':
        print('You won, you get a point.')
        man_score += 1
    if man == 'scissors'and computer == 'stone':
        print('I won, I get a point.')
        computer_score += 1

    print("The current score is:")
    print("Me " + str(computer_score) + " - " + str(man_score) + " You")

if (man_score == 3):
    print('You won, you get: ', money, '$')
else:
    print('I won, you lose', money, '$')

