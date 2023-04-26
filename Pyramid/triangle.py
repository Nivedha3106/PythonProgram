n = int(input("Enter the number of rows: "))
num = 1
for i in range(n+1): #row iteration
    for j in range (n-i-1): #print space
        print(" ", end=" ")
    for k in range(i+1): #print current row
        print("{:02d}".format(num),end = " ")
        num+=1
    print()
