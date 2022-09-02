# Activity 4: Write a Python program that ask user to input two numbers. Check if both numbers are divisible by 2 or 3, if yes multiply them and print them on screen. If not, add them and then print it on screen.

# I didn't write this code myself, but I watched and listened throughout the process of this code being written. I feel like I understand some of the reasonings for the way this piece of code was written, but I don't have enough confidence to write my own code based on what I learned from this exercise yet.

i = 0 # i is a temporary variable that refers to the current iteration  of the loop. We start at 0 because it is the first iteration.
while i < 3: # The while loop executes a set of statements as long as a condition is true. The code will run 3 times to match the example output in the exercise.
    user_input = input("Enter two integers: ") 
    index_of_comma = user_input.find(",") # This line finds the index of the comma and puts it into a variable.
    number_in_string1 = (int(user_input[0:index_of_comma])) # To separate the first number from the second number in the user input, this line takes whatever data there is between index 0 and the index of the comma and puts that into variable number_in_string1.
    number_in_string2 = (int(user_input[index_of_comma+1:])) # Same thing for the second number, except it takes everything from one index after the comma.
    answer = 0
    # The % is an operator that returns the remainder when a is divided by b. In this case, we are trying to see if it returns 0 when both numbers are divided by either 2 or 3. If it returns 0, they are divisble by 2 or 3, and the code will execute number_in_string1 * number_in_string2 and return an answer. If it doesn't return 0, it will execute number_in_string1 + number_in_string2.
    if (number_in_string1%2 == 0 and number_in_string2%2 == 0) or (number_in_string1%3 == 0 and number_in_string2%3 == 0) :
        answer = number_in_string1 * number_in_string2
        print("Both Numbers are divisible by 2 or 3")
    else:
        answer = number_in_string1 + number_in_string2
        print("Both numbers aren't divisible by 2 or 3")
    print(answer,"\n") # “\n” is used to create a new line
    i+=1 # This line adds another iteration once the code is executed. It will only run 3 times because the while loop only allows the code to be executed as long as i < 3
