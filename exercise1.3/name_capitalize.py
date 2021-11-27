text = "I like apples"


def my_func():
    # We'll try joining another string to 'text'
    global text
    text = text + "... but I love oranges better!"
    print("text from the inside: " + text)


my_func()
print("text from the outside: " + text)
# for num in range(10, 60, 10):
#     print(num)

# number = 10
# while number < 60:
#     print("lll", number)
#     number += 10

# test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]
# test_scores.sort(reverse=True)
# for value in range(0, 3):
#     print(test_scores[value])

# first_value = int(input("Enter the first value: "))
# second_value = int(input("Enter the second value: "))
# operator = str(input("Enter the operator: "))
# result = 0
# if operator == "+":
#     result = first_value + second_value
#     print(result)
# elif operator == "-":
#     result = first_value - second_value
#     print(result)
# else:
#     print("Invalid operator")


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# first_name = first_name.capitalize()
# last_name = last_name.capitalize()

# print("Your name is", first_name, last_name)
