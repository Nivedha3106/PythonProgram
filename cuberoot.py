# Write a program to find the cube root of a number without using any readily available modules 

# n = int(input("Enter a number: "))
# print ("cube root of,",n, "is :", n ** (1/3))

def cuberoot(num):
    
    guess = num / 3.0  
    step = 0.0000001 

    while abs(guess**3 - num) > step:
        guess = guess - (guess**3 - num) / (3 * guess**2)
    return round(guess, 7)

num = float(input("Enter a number: "))

result = cuberoot(num)

print(f"The cube root of {num} is {result}")

