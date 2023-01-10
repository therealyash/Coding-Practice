'''
You are given a string. Split the string on a " " (space)
delimiter and join using a - hyphen.
#>>> a = this is a string
#>>> a = a.split( ) # a is converted to a list of strings.
#>>> print a
['this', 'is', 'a', 'string']
'''

def split_and_join(line):
    # write your code here
    lst = line.split(" ")
    new_str = "-".join(lst)
    return new_str

if __name__ == '__main__':


