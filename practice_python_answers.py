#Question 1:
name,age = input('Enter your name: '),int(input('Enter your age'))
print(f'Hello {name}! In the year {2022+(100-age)}, you will be 100 years old!')

#Question 2
user_input = int(input('Enter a number: '))
if user_input % 4 == 0:
    print(f'{user_input} is a multiple of four')
elif user_input % 2 == 0:
    print(f'{user_input} is even')
else:
    print(f'{user_input} is odd')
num,check = int(input('Enter a Dividend: ')),int(input('Enter a Divisor: '))
if num % check == 0:
    print(f'{num} is divisible by {check}')
else:
    print(f'{num} is not divisible by {check}')

#Question 3
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_lst = []
for item in lst:
    if item < 5:
        new_lst.append(item)
        print(item)
print(new_lst)
print([item for item in lst if item < 5])
user_input = int(input('Enter a number: '))
print([item for item in lst if item < user_input])

#Question 4
user_input = int(input('Enter a number: '))
for i in range(1,user_input+1):
    if user_input % i == 0:
        print(i)

#Question 5
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_lst = []
rand_lst1 = []
rand_lst2 = []
newer_lst = []
test_lst = []
for item in a:
    if item in b and item not in new_lst:
        new_lst.append(item)
print(new_lst)
for _,_ in enumerate(a):
    num = random.randint(min(a+b),max(a+b))
    rand_lst1.append(num)
for _,_ in enumerate(a):
    num = random.randint(min(a+b),max(a+b))
    rand_lst2.append(num)
for item in rand_lst1:
    if item in rand_lst2 and item not in newer_lst:
        newer_lst.append(item)
print(newer_lst)

print(sorted(list(set(a+b))))

#Question 6
user_input = input('Enter a word: ')
if user_input == user_input[::-1]:
    print(f'{user_input} is a palindrome')
else: print(f'{user_input} is not a palindrome')

#Question 7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([item for item in a if item % 2 == 0])

#Question 8
lst = ['rock','paper','scissors']
while True: 
    while True:
        user_game = input('Do you want to start a new game?: (Y/N) ').lower()
        if user_game in ['n','y']: break
        print('Error: Invalid Input')
    if user_game in ['n']: break
    user_choice = input('Enter rock, paper, or scissors: ').lower()
    computer_choice = random.choice(lst)
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print(f'The computer chose {computer_choice}')
        print('You Win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print(f'The computer chose {computer_choice}')
        print('You Win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'The computer chose {computer_choice}')
        print('You Win!')
    else:
        print(f'The computer chose {computer_choice}')
        print('You Lose!')

#Question 9
import random
rand_num = random.randint(1,9)
user_input = input('Enter a guess: ')
if user_input == 'exit':
    quit()
user_input = int(user_input)
count = 1
while user_input != rand_num and user_input != 'exit':
    count += 1
    if user_input > rand_num:
        print('Too High!')
    else: print('Too Low!')
    user_input = input('Enter a guess: ')
    if user_input == 'exit': break
    user_input = int(user_input)
if user_input == rand_num:
    print(f'Correct! You guessed this in {count} guess/guesses!')

#Question 10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
[c.append(item) for item in a if item in c]
print(c)

#Question 11
def isPrime(num):
    factor_lst = [i for i in range(2,num+1) if num % i == 0]
    if factor_lst == [num]: return(True)
    return(False)
user_input = int(input('Enter a number: '))
isPrime(user_input)

#Question 12
a = [5,10,15,20,25]
def first_last(lst):
    return [lst[0],lst[-1]]
first_last(a)

#Question 13
def Fibonacci(count):
    lst = []
    previous_num,num = 0,1
    if count < 0:
        print('ERROR: Enter a positive number')
    if count == 0:
        return([previous_num])
    for i in range(count):
        lst.append(previous_num)
        nth = previous_num + num
        previous_num = num
        num = nth
    return(lst)
user_input = int(input('How many fibonacci numbers do you want?: '))
Fibonacci(user_input)

#Question 14
lst = [random.randint(1,10) for i in range(15)]
def duplicate_removal(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return(new_lst)
def duplicate_removal_2(lst):
    return(list(set(lst)))

#Question 15
def reverse_sentence(s1):
    return(' '.join((s1.split()[::-1])))
reverse_sentence('I love potatoes')

#Question 16
import string
letters = string.ascii_letters
symbols = '&%^$#@!'
digits = string.digits
char_lst = list(letters+symbols+digits)
user_input = int(input('How long do you want your password to be?: '))
new_string = ''
for _ in range(user_input):
    new_string+=random.choice(char_lst)
print(new_string)

#Question 17
from urllib.request import urlopen
from bs4 import BeautifulSoup
html_data = urlopen('https://www.nytimes.com/').read().decode()
soup = BeautifulSoup(html_data,'html.parser')
tags = soup.find_all('h3',class_= "indicate-hover css-1pvrrwb")
for tag in tags[:7]:
    print(tag.contents[0])

#question 18
import random
correct_num = str(random.randint(1000,9999))
print(correct_num)
print('Welcome to the Cows and Bulls Game!')
user_guess = input('Enter a guess: ')
guess_count = 1
while user_guess != correct_num:
    cow,bull = 0,0
    for i in range(4):
        if user_guess[i] == correct_num[i]:
            cow += 1
        elif user_guess[i] in correct_num:
            bull += 1
    guess_count += 1
    print(f'{cow} cows, {bull} bulls!')
    user_guess = input('Enter a guess: ')
cow,bull = 4,0
print(f'{cow} cows, {bull} bulls!')
print(f'You guessed the number in {guess_count} guesses')

#Question 19
import requests
from bs4 import BeautifulSoup
html_data = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture').text
soup = BeautifulSoup(html_data,'html.parser')
text = soup.get_text()
text[text.find('It was early 2001'):text.find('Monica Lewinsky Is Back1')]

#Question 20
from statistics import median
from math import ceil
def search(lst,num):
    if num in lst: return(True)
    return(False)
#user_input = int(input('Enter a number: '))
lst = list(range(10))
search(lst,user_input)
def binary_search(lst,num):
    med = median(lst)
    if num <= int(med):
        if num in lst[:lst.index(int(med))+1]: return(True)
        else: return(False)
    elif num >= ceil(med):
        if num in lst[lst.index(ceil(med)):]: return True
        else: return(False)
binary_search(lst,5)

#Question 21
html_data = requests.get('https://www.nytimes.com/').text
soup = BeautifulSoup(html_data,'html.parser')
tags = soup.find_all('h3',class_="indicate-hover css-1pvrrwb")
with open('NYT_headings.txt','w') as fh:
    for tag in tags:
        fh.write(tag.contents[0])
    
#Question 22
html_data_one = requests.get('https://www.practicepython.org/assets/nameslist.txt').text
name_dict = {}
for name in html_data_one.splitlines():
    name_dict[name] = name_dict.get(name,0) + 1
for key,val in name_dict.items():
    print(key,val)
html_data_two = requests.get('https://www.practicepython.org/assets/Training_01.txt').text
type_dict = {}
for line in html_data_two.splitlines():
    type_dict[line.split('/')[2]] = type_dict.get(line.split('/')[2],0) + 1
for key,val in type_dict.items():
    print(key,val)

#Question 23
prime_nums = requests.get('https://www.practicepython.org/assets/primenumbers.txt').text.splitlines()
happy_nums = requests.get('https://www.practicepython.org/assets/happynumbers.txt').text.splitlines()
inner_join = []
for item in happy_nums:
    if item in prime_nums:
        inner_join.append(item)
print(inner_join,len(inner_join))

#Question 24
def print_horizontal_line():
    print(" --- " * dimensions)
def print_vertical_line():
    print("|   " * (dimensions + 1))
dimensions = int(input('How large do you want to board to be?'))
for i in range(dimensions):
    print_horizontal_line()
    print_vertical_line()
print_horizontal_line()

#Question 25
from statistics import mean
print('Think of a number between 1 and 100 inclusive... The Computer Will Try to Guess It')
correct_num = int(input('Enter a number: '))
guess_history = [1,100]
computer_guess = 50
guess_count = 1
print(f'The Computer Guesses {computer_guess}')
while computer_guess != correct_num:
    if computer_guess < correct_num:
        print('Too Low!')
        guess_history[0] = computer_guess
    elif computer_guess > correct_num:
        print('Too High!')
        guess_history[1] = computer_guess
    guess_count += 1
    computer_guess = round(mean(guess_history))
    print(guess_history)
    print(f'The Computer Guesses {computer_guess}')
print(f'The computer guessed your number of {correct_num} in {guess_count} tries')

#Question 26
def horizontal_match(matrix):
    for array in matrix:
        if set(array) in [{1},{2}]:
            return(array[0])

def left_to_right_diag_match(matrix):
    diag_array = []
    for i, _ in enumerate(matrix):
        diag_array.append(matrix[i][i])
    if set(diag_array) in [{1},{2}]:
        return(diag_array[0])

def right_to_left_diag_match(matrix):
    diag_array = []
    for count,index in enumerate(range(-1,(-1-len(matrix)),-1)):
        diag_array.append(matrix[count][index])
    if set(diag_array) in [{1},{2}]:
        return(diag_array[0])

def vertical_match(matrix):
    for i, _ in enumerate(matrix):
        vertical_array = []
        for array in matrix:
            vertical_array.append(array[i])
        if set(vertical_array) in [{1},{2}]:
            return(vertical_array[0])

#Question 27
matrix = [[0,0,0],
        [0,0,0],
        [0,0,0]]

user_input = input('Enter the coordinates of your move: ')
coords = tuple((int(num) for num in user_input.split(',')))
while coords[0] not in range(len(matrix)) or coords[1] not in range(len(matrix)):
    print('ERROR: Coordinates not in range of matrix')
    user_input = input('Enter the coordinates of your move: ')
    coords = tuple((int(num) for num in user_input.split(',')))
matrix[coords[0]][coords[1]] = 'x'
for array in matrix:
    print(array)

#Question 28
def max_three(val1,val2,val3):
    tup = (val1,val2,val3)
    for count,value in enumerate(tup):
        if count == 0:
            maximum = value
        if value > maximum:
            maximum = value
    return(maximum)
max_three(1234,6532,54324)

import random
import time

def horizontal_match(matrix):
    for array in matrix:
        if set(array) in [{'X'},{'O'}]:
            return(array[0])

def left_to_right_diag_match(matrix):
    diag_array = []
    for i, _ in enumerate(matrix):
        diag_array.append(matrix[i][i])
    if set(diag_array) in [{'X'},{'O'}]:
        return(diag_array[0])

def right_to_left_diag_match(matrix):
    diag_array = []
    for count,index in enumerate(range(-1,(-1-len(matrix)),-1)):
        diag_array.append(matrix[count][index])
    if set(diag_array) in [{'X'},{'O'}]:
        return(diag_array[0])

def vertical_match(matrix):
    for i, _ in enumerate(matrix):
        vertical_array = []
        for array in matrix:
            vertical_array.append(array[i])
        if set(vertical_array) in [{'X'},{'O'}]:
            return(vertical_array[0])

def draw_board():
    print(f'''
    1   2   3
   --- --- ---
1 | {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} |   
   --- --- ---
2 | {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} |   
   --- --- ---
3 | {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} |   
   --- --- ---''')

matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

h_check = None
v_check = None
diag_check_one = None
diag_check_two = None

draw_board()
while ' ' in set(matrix[0]) or ' ' in set(matrix[1]) or ' ' in set(matrix[2]):
    user_input = input('Enter the coordinates of your move (row,col): ')
    coords = tuple((int(num)-1 for num in user_input.split(',')))
    while coords[0] not in range(len(matrix)) or coords[1] not in range(len(matrix)) or matrix[coords[0]][coords[1]] != ' ':
        print('ERROR: INVALID MOVE')
        user_input = input('Enter the coordinates of your move: ')
        coords = tuple((int(num) for num in user_input.split(',')))
    matrix[coords[0]][coords[1]] = 'X'
    
    draw_board()

    h_check = horizontal_match(matrix)
    v_check = vertical_match(matrix)
    diag_check_one = left_to_right_diag_match(matrix)
    diag_check_two = right_to_left_diag_match(matrix)
    if h_check is not None or v_check is not None or diag_check_one is not None or diag_check_two is not None:
        break

    time.sleep(1)
    
    while True:
        computer_move = (random.randint(0,2),random.randint(0,2))
        if matrix[computer_move[0]][computer_move[1]] == ' ':
            matrix[computer_move[0]][computer_move[1]] = 'O'
            break
    
    draw_board()

    h_check = horizontal_match(matrix)
    v_check = vertical_match(matrix)
    diag_check_one = left_to_right_diag_match(matrix)
    diag_check_two = right_to_left_diag_match(matrix)
    if h_check is not None or v_check is not None or diag_check_one is not None or diag_check_two is not None:
        break

if h_check == 'X' or v_check == 'X' or diag_check_one == 'X' or diag_check_two == 'X':
    print('CONGRATULATIONS! YOU WIN!')
elif h_check == 'O' or v_check == 'O' or diag_check_one == 'O' or diag_check_two == 'O': 
    print('SORRY, YOU LOST!')
else: print('THERE WAS A DRAW!')

#Question 30
import requests
import random
html_data = requests.get('http://norvig.com/ngrams/sowpods.txt').text.splitlines()
random_word = random.choice(html_data)
print(random_word)

#Question 31
print('Welcome to Hangman!')
word_lst = list(random_word)
dashes = ['_' for item in word_lst]
past_guesses = []
guess_count = 0
while dashes != word_lst and guess_count < 6:
    print(' '.join(dashes))
    user_guess = input('Enter a guess: ').upper()
    while user_guess in past_guesses:
        user_guess = input('Enter a guess: ').upper()
    past_guesses.append(user_guess)
    if user_guess in word_lst:
        for i , _ in enumerate(dashes):
            if word_lst[i] == user_guess:
                dashes[i] = user_guess
    else: 
        guess_count += 1
        print('INCORRECT!')
print(' '.join(dashes))
if guess_count == 6:
    print('YOU LOSE!')
else:
    print('YOU WIN!')

#Question 32
print('Welcome to Hangman!')
word_lst = list(random_word)
dashes = ['_' for item in word_lst]
past_guesses = []
guess_count = 0
while dashes != word_lst and guess_count < 6:
    print(' '.join(dashes))
    user_guess = input('Enter a guess: ').upper()
    while user_guess in past_guesses:
        user_guess = input('Enter a guess: ').upper()
    past_guesses.append(user_guess)
    if user_guess in word_lst:
        for i , _ in enumerate(dashes):
            if word_lst[i] == user_guess:
                dashes[i] = user_guess
    else: 
        guess_count += 1
        print('INCORRECT!')
print(' '.join(dashes))
if guess_count == 6:
    print('YOU LOSE!')
else:
    print('YOU WIN!')
new_game = input('Do you want to start a new game? (Y/N): ').lower()
if new_game == 'n':
    quit()

#Question 33
birthday_dic = {'Preston':'05/02/2002','Carys':'11/02/2006','David Beckham':'05/02/1980'}
user_selection = input('Whose birthday do you want to look up? ')
print(f'{user_selection}\'s birthday is {birthday_dic[user_selection]}.')

#Question 34

import json

with open('Birthday_info.json','r') as fh:
    data = json.load(fh)

def add_entry(data):
    name = input('Who do you want to add to the dictionary?: ')
    value = input('Enter the birthday of your person')
    data[name] = value
    with open('Birthday_info.json','w') as fh:
        json.dump(data,fh)

add_entry(data)

#Question 35
import json
with open('Birthday_info.json','r') as fh:
    data = json.load(fh)

count_dic = {}

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

for value in data.values():
    month = int(value.split('/')[0])
    count_dic[num_to_string[month]] = count_dic.get(num_to_string[month],0) + 1
print(count_dic)

#Question 36
from bokeh.plotting import figure, show, output_file

output_file('Count_Histogram.html')
x_categories = list(num_to_string.values())
x = list(count_dic.keys())
y = list(count_dic.values())
p = figure(x_range = x_categories)
p.vbar(x=x,top=y,width=0.5)
show(p)

#Question 37
def tic_tac_toe_grid(dimensions):
    for i in range(dimensions):
        print(" ---" * dimensions)
        print("|   " * (dimensions + 1))
    print(" ---" * dimensions)

user_input = int(input('What size dimensions do you want you grid to be?:' ))

tic_tac_toe_grid(user_input)

#Question 38
user_input = input('What is your name and age separated by a comma?: ')
name_age = user_input.split(',')
name_age[1] = int(name_age[1])
print(f'Hello {name_age[0]}! In {100-name_age[1]} years, you will be 100!')