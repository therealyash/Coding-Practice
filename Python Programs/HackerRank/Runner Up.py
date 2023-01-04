# Find the Runner Up Score from the given list

n = int(input('Enter a number: '))
arr = map(int, input().split())

print(sorted(set(arr), reverse=True)[1])




