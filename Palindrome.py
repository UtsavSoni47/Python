num = input("Enter a number: ")
rev = num[::-1]

print("Reversed number:", rev)

if num == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
