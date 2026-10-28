#Write a program to create a pyramid of the character ‘*’ and a reverse pyramid
n=int(input("Enter the number:")
rows = n
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

print()

for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '* ' * i)

#OUTPUT 
1].
Enter the number:5
    *
   * *
  * * *
 * * * *
* * * * *

* * * * *
 * * * *
  * * *
   * *
    *

[Program finished]

2].
Enter the number:8
       *
      * *
     * * *
    * * * *
   * * * * *
  * * * * * *
 * * * * * * *
* * * * * * * *

* * * * * * * *
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *

[Program finished]
