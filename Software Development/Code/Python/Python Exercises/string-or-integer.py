# Activity 3: Write a Python program to check a whether a string represents an integer or not.

# I lost my first attempts at this exercise but it more or less looked like variations of this:
input_from_user = (input("Input a string: "))
                   if input_from_user = int
                   print("The string is an integer")
                   elif input_from_user = str
                   print("The string is not an integer")
                
# I tried many different things but the main issue was that the program would always read the user input as a string, even if they enter a number.
# I figured I could fix this by forcing the input to be an integer, otherwise it would come up with an error. An error would mean the input is anything other than an integer. If the error message is displayed, I will ask the program to display "The string is not an integer". If no error is displayed, "The string is an integer" will be displayed.

# Try lets you check a code for errors. The except block lets you handle the error. If an error occurs, the program will go to the except block.
try: 
    input_from_user = type(int(input("Input a string: "))) # The input will be read as an integer. If not, it will come up with a ValueError.
except ValueError: 
    print("The string is not an integer")
else: # The code is executed when there is no error i.e. the input is an integer
    print("The string is an integer")
