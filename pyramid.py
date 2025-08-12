# Number of rows for the pyramid
s = 5

for i in range(1, s + 1):
    # Print spaces
    print(' ' * (s - i), end='')
    # Print stars
    print('*' * (2 * i - 1))

