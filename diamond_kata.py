import re

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#get input
user_input = input("Please enter a valid, capitalised letter from B - Z: ")

#check input
while len(user_input) != 1 or not user_input.isalpha() or not user_input.isupper() or 'A' in user_input:
    user_input = input("Please enter a valid, capitalised letter from B - Z: ")

length = alphabet.index(user_input)

#print top half of diamond
for x in range(length):
    if x == 0:
        print(' '*(length - x) + alphabet[x])
    else:
        print(' '*(length - x) + alphabet[x] + ' '*(2*x-2) + ' ' + alphabet[x])

#print bottom half of diamond
y = length
while y >= 0 :
    if y == 0:
        print(' '*(length - y) + alphabet[y])
    else:
        print(' '*(length - y) + alphabet[y] + ' '*(y*2 - 1) + alphabet[y])
    y -= 1