"""
You are given a string and your task is to swap cases. In other
words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
"""
def swap_case(s):
    new_str = ''
    for i in s:
        if i.islower():
            new_str = new_str + i.upper()
        else:
            new_str = new_str + i.lower()

    return new_str
s = input('Enter a string to swap: ')
print(swap_case(s))