def cube_root(num):

    left = 0
    right = num

    while left <= right:

        mid = (left + right) / 2

        if abs(mid**3 - num) < 0.0001:
            return mid
        elif mid**3 < num:
            left = mid
        else:
            right = mid
    return None
    
print(cube_root(int(input("Enter a number: "))))