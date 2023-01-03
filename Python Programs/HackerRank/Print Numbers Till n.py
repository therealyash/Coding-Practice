"""
Take input n from user and print numbers till n in string format
Ex - 
I/P
n = 4

O/P
'1234'
"""

n = int(input('Enter a number: '))
new_str =''
i = 0
while i < n:
    i += 1
    new_str = new_str + str(i) 
    
print(new_str)




