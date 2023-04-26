# Write a program to print a pyramid with consecutive numbers 

n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n+1): #row iteration
    for j in range(1, i+1): #column iteration
        print(num, end=" ")
        num+=1
    print()