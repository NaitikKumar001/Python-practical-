'''Write a function that prints a dictionary where the keys are numbers between 1 and 5
and the values are cubes of the keys.'''

n=(int(input("Enter the number:")
       
def cube():
    cub = {}
    for i in range(1,n+1):
        c = i**3
        cub.update({i:c})
    print(cub)
cube()

#OUTPUT 
1].
Enter the number:5
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

[Program finished]

2].
Enter the number:10
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}

[Program finished]
