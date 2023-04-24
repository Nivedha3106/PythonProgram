# Write a program to find the cube root of a number without using any readily available modules 

# n = int(input("Enter a number: "))
# print ("cube root of,",n, "is :", n ** (1/3))


cube = int(input())
epsilon =0.1
guess = 0
inc = 0.001
num_guess = 0
while(abs(guess**3 - cube)>= epsilon):
    if (abs(guess**3)) > cube: 
        break
        
    guess += inc
    num_guess += 1
    

# print(num_guess)
if (abs(guess**3 - cube)>= epsilon):
    print("Failed to check the cube")
else: 
    print(guess)


