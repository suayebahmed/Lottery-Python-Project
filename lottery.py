import math
import random


# Function 1
def num_possible_tickets(k, n, m):
    numerator = 1
    i = n
    while i >= n - k + 1:
        numerator *= i
        i -= 1
    denominator = math.factorial(k)

    return m * (numerator // denominator)


# Function 2
def get_player_numbers(k, n):
    print(f'Pick your {k} distinct numbers!')
    nums_list = []
    for i in range(k):
        usr_inp = int(input(f'Enter number {i + 1} (must be 1-{n}, cannot repeat): '))
        if (usr_inp in nums_list) or (not 1 <= usr_inp <= n):
            while usr_inp in nums_list:
                usr_inp = int(input(f'Error - you’ve already entered {usr_inp}.  Try again: '))
                while not 1 <= usr_inp <= n:
                    usr_inp = int(input(f'Error - number must be between 1 and {n}.  Try again: '))

            while not 1 <= usr_inp <= n:
                usr_inp = int(input(f'Error - number must be between 1 and {n}.  Try again: '))
                while usr_inp in nums_list:
                    usr_inp = int(input(f'Error - you’ve already entered {usr_inp}.  Try again: '))
        nums_list.append(usr_inp)
    return nums_list


# Function 3
def get_player_bonus(m):
    usr_inp = int(input(f'Now pick your bonus number (must be 1-{m}): '))
    while not 1 <= usr_inp <= m:
        usr_inp = int(input(f'Error - bonus number must be between 1 and {m}.  Try again: '))
    return usr_inp


# Function 4
'''
Randomly generates k distinct integers between 1 and n (inclusive). 
The results should be returned in a 1D list of length k.
'''


def get_drawn_numbers(k, n):
    return random.sample(range(1, n), k)


# Function 5
def get_drawn_bonus(m):
    return random.randint(1, m)


# Function 6
def print_ticket(list_distinct, bonus):
    for i in range(len(list_distinct)):
        for j in list_distinct[i]:
            print(f'{j}\t', end='')
        print(f'||\tBonus: {bonus[i]}')


# Function 7
def count_matches(list_a, list_b):
    count = 0
    for i in list_a:
        for j in list_b:
            if i == j:
                count += 1
    return count


###############################################
# END OF ALL REQUIRED FUNCTIONS
###############################################

# PART 8
# Beginning Intro
print('DESIGN-A-LOTTO v1.0')
print('-------------------')
print()
print('*******')
print("First, let's set up the game!")
print()

# Get user input for k, n, m and validate those values with loop
k = int(input("How many distinct numbers should the player pick? "))
while not k >= 1:
    k = int(input('ERROR - number(s) must to be at least 1: '))
print()

n = int(input(f"Ok, Each of those {k} numbers should be range from 1 to what? "))
while n < k:
    n = int(input(f'Error - range must be at least 1 to {k} to have a valid game.  Try again: '))
print()

m = int(input('OK. And finally, the bonus number should range from 1 to what? '))
while not m >= 1:
    m = int(input('Error - range must be at least 1 to 1 to have a valid game.  Try again: '))
print()
print("*******")

# Show possible tickets and possible winning chance
print(f'There are {num_possible_tickets(k, n, m)} possible tickets in this game.'
      f'Each ticket has a {1 / num_possible_tickets(k, n, m)} chance of winning the jackpot.'
      f'Lets play, good luck!')
print()

# user input for number of tickets user want to buy
ticket_num = int(input('How many tickets would you like to buy? '))
while not ticket_num >= 1:
    ticket_num = int(input('Must be greater than 0, try again: '))
print()

# 2d list of all tickets and 1d list of bonus numbers
ticket_2d_list = []
bonus_1d_list = []
for i in range(ticket_num):
    print(f"* Ticket #{i + 1} of {ticket_num} *")
    print()
    list_distinct = get_player_numbers(k, n)
    print()
    bonus = get_player_bonus(m)
    print()
    ticket_2d_list.append(list_distinct)
    bonus_1d_list.append(bonus)

    print('Your ticket so far:')
    print('-------------------')
    print_ticket(ticket_2d_list, bonus_1d_list)

# Simulating Lottery draw
drawn_nums = get_drawn_numbers(k, n)
drawn_bonus = get_drawn_bonus(m)

# Showing drawn numbers.
print()
print('********')
print('The moment of truth has arrived! Here are the drawn numbers:')


def show_drawn_and_best_numbers(nums, bonus_num):
    for i in nums:
        print(f'{i}\t', end='')
    print(f'||\tBonus: {bonus_num}')


show_drawn_and_best_numbers(drawn_nums, drawn_bonus)

print()
print()

# best ticket
total_num_match = []
for i in range(len(ticket_2d_list)):
    if count_matches(ticket_2d_list[i], drawn_nums) > 0:
        total_num_match.append(count_matches(ticket_2d_list[i], drawn_nums))


bon_n = False
for i in bonus_1d_list:
    if i == drawn_bonus:
        match_bonus_ind = bonus_1d_list.index(i)
        bonus_num_matched = i
        bon_n = True


if total_num_match == []:
    print('Your best ticket(s): ')
    print('No matches\n')
    print(f'You matched 0/{k} drawn numbers')


    if bon_n == True:
        print('You matched the bonus num')
    else:
        print('You did not match the bonus number.')

    print('Sorry, no jackpot this time.  Really, did you expect anything else?')

else:
    max_value = max(total_num_match)
    indices = [index for index, value in enumerate(total_num_match) if value == max_value]

    print('Your best ticket(s):')
    for i in indices:
        for j in ticket_2d_list[i]:
            print(f'{j}\t', end='')
        print(f'||\tBonus: {bonus_1d_list[i]}')

    print(f'You matched {max_value}/{k} drawn numbers')


    if bon_n == True:
        print('You matched the bonus num')
    else:
        print('You did not match the bonus number.')

    if k == max_value and bon_n == True:
        print('You wins the jackpot.')
    else:
        print('Sorry, no jackpot this time.  Really, did you expect anything else?')


# END OF CODE
