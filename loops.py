# Program for Table of any number
'''
    num = int(input("Numbe for Table: "))

    i = 1
    while(i <= 10):
        print(f'{num} x {i} = {num*i}')
        i+=1
'''

# Program for Greeting the users whose name start with S
'''
    l = ["Harry", "Soham", "Sachin", "Rahul"]

    for i in range(len(l)):
        name = l[i]
        if('S'.lower() in name[0].lower()):
            print(f"Hii {name}")
'''

# Program for getting prime number

'''
    num = int(input("Prime Number: "))
    for i in range(2, num):
        if(num%i == 0):
            print(f'{num} is not Prime Number')
            break
    else:
        print(f'{num} is Prime Number')
'''

# Program for getting factorial number of given number
'''
    num = int(input("Factorial Number: "))
    product = 1
    for i in range(1, num+1):
        product = product * i

    print(f'Factorial of {num} is {product}')
'''
# Program for star pattern when num is any number
 
num = int(input("Factorial Number: "))
# for i in range(1, num+1):
#     print(' '*(num - i) + '*'*(2*i-1))

# for i in range(1, num+1):
#     print('*'*i)

for i in range(1, num+1):
    if(i == 1 or i == num):
        print('*'*num)
    else:
        print('*'+' '*(num-2)+'*')