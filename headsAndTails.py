## headsAndTails.py
import random
number_of_streaks = 0

#SET UP AND EMPTY LIST TO CAPTURE THE FOR LOOP RESULTS

output = []

#FUNCTION RUN THE MOCK COIN FLIPS
def results():
    for i in range (100000000):
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            coin_flip = 'H'
            output.append(coin_flip)
        else:
            coin_flip = 'T'
            output.append(coin_flip)

results()

#IMPRESS HALLIE WHILE NUMBERS RUN ON MY COMPUTER
print(output)

#CONVERT THE OUTPUT LIST TO A STRING
string = ''.join(output)

#SEARCH THROUGH THE RESULTS OF THE STRING FOR THE OCCURANCES OF THE
#HEADS AND TAILS STREAKS
t_occurance = string.count('TTTTTT')
h_occurance = string.count('HHHHHH')

#ADD STREAKS TOGETHER TO GET THE FINAL NUMBER OF STREAKS
number_of_streaks = t_occurance + h_occurance
print(number_of_streaks)
