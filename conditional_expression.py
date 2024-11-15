# Which number is greater
'''
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    n3 = int(input('Enter Third number: '))

    if (n1 > n2 and n1 > n3):
        print(f'{n1} number is greater than {n2} {n3}')
    elif (n2 > n1 and n2 > n3):
        print(f'{n2} number is greater than {n1} {n3}')
    else:
        print(f'{n3} number is greater than {n1} {n2}')
'''

# Find grade according to percentage

maths = int(input("Total marks in maths: "))
science = int(input("Total marks in science: "))
english = int(input("Total marks in english: "))

total_percentage = (100*(maths + science + english))/300

if(total_percentage >= 90 and total_percentage <= 100):
    print(f"{total_percentage}% then Grade A+")
elif(total_percentage >= 80 and total_percentage <= 90):
    print(f"{total_percentage}% then Grade A")
elif(total_percentage >= 70 and total_percentage <= 80):
    print(f"{total_percentage}% then Grade B")
elif(total_percentage >= 35 and total_percentage <= 70):
    print(f"{total_percentage}% then Grade D")
else:
    print(f"{total_percentage}% then Grade F you are fail")

