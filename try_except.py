# try:
#     with open('oops.py', 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open('python.py', 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# In a/b if b is zero then handle error using zero division error

a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError as error:
    print("Infinite")