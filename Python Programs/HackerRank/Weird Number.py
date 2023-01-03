

N = int(input('Enter a number: ').strip())

    

if N % 2:
    print('Weird')
elif not (N % 2) and N >= 2 and N <= 5:
    print('Not Weird')
elif not (N % 2) and N >= 6 and N <= 20:
    print('Weird')
elif not (N % 2) and N > 20:
    print('Not Weird')
