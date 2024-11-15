# Function to print sum of n natural number

def sum(n):
    if(n == 1): return 1
    return sum(n-1) + n


# Function for star pattern when num is any number

def star_pattern(n):
    if(n == 0): return
    print('*'* n)
    star_pattern(n-1)

num = int(input("Enter Natural Number: "))
star_pattern(num)