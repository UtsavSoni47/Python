print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # start from 2 because 1 is not a prime number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
