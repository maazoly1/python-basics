# make a list which contains multiplication of users input numbers

num = float(input("Enter a number: "))
table = [ i*num for i in range(1, 11)]

print(table)

with open("table.txt", "a") as f:
    f.write(f"Table of {num} = {str(table)}")