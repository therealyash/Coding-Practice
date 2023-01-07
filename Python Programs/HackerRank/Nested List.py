# Nested List

"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
"""

result = []
score_list = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result+=[[name,score]]
        score_list+=[score]
    b=sorted(list(set(score_list)))[1]
    for a,c in sorted(result):
        if c==b:
            print(a)