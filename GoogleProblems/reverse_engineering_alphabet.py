alphabet = "abcdefghijklmnopqrstuvwxyz"

# The string but reversed
reverse = alphabet[::-1]

#Creat a tuple from the string and reversed string, and create a dictionary from it
alphabet_dict = dict(zip(alphabet, reverse))

# To be edited
input = "test"


reversed = ''.join(alphabet_dict[c] for c in )