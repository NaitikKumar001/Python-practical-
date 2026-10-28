'''Write a program to accept a number ‘n’ and
a. Check if ’n’ is prime'''

prime = True

n = int(input("Enter a number:"))

if n <= 1:
    prime = False
elif n == 2:
    prime = True
elif n%2 == 0:
    prime = False


if prime:
    print("The Number is Prime.")
else:
    print("The Number is NOT Prime.")

#OUTPUT
1].
Enter a number:97
The Number is Prime.

[Program finished]

2].
Enter a number:1804
The Number is NOT Prime.

[Program finished]
  
