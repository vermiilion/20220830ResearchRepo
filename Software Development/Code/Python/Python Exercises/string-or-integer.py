try:
    input_from_user = type(int(input("Input a string: ")))
except ValueError:
    print("The string is not an integer")
else:
    print("The string is an integer")
