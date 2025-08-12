num = input("Enter a number: ")
n = len(num)
total = sum(int(digit) ** n for digit in num)

if total == int(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
