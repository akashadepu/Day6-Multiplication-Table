#                      Day6-Multiplication-Table

user_input = int(input("Enter a number: "))

user_limit = int(input("Enter number till where you need: "))

for i in range(1,user_limit + 1):
    print(f"{user_input} * {i} = {user_input * i}")