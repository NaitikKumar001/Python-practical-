'''5. Write a program to perform the following operations on a string
a. Find the frequency of a character in a string.
b. Replace a character by another character in a string.
c. Remove the first occurrence of a character from a string.
d. Remove all occurrences of a character from a string.
'''
count = 0

string = input("Enter a string:")

#a

ch = input("Enter a character:")
for i in string:
    if i == ch:
        count+=1    
print("The Character", ch ,"appeared", count ,"times")

#b

c1 = input("Enter a character to be replaced:")
c2 = input("Enter the character to be replaced with:")
print(string.replace(c1, c2))

#c

rem = input("Enter a character to be removed:")
print(string.replace(rem, "", 1))

#d

rem_all = input("Enter a character to remove its all occurence:")
print(string.replace(rem_all, ""))

#OUTPUT 
1].
-Enter a string:"63,872,1,3,2,3,90,63,2,8,5,3,.8,1,5"
-Enter a character:3

The Character 3 appeared 5 times

-Enter a character to be replaced:5
-Enter the character to be replaced with:6

"63,872,1,3,2,3,90,63,2,8,6,3,.8,1,6"

-Enter a character to be removed:872

"63,,1,3,2,3,90,63,2,8,5,3,.8,1,5"

-Enter a character to remove its all occurence:8

"63,72,1,3,2,3,90,63,2,,5,3,.,1,5"

[Program finished]
