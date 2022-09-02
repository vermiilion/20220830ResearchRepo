# Activity 2: Convert a month name to a number of days.

# Initially, this was the code I had written for this exercise:

month = input("Input the name of Month: ")
if month == "January" "March" "May" "July" "August" "October" "December":
   print("No. of days: 31 days")
elif month == "April" "June" "September" "November":
   print("No. of days: 30 days")
elif month == "February":
   print("No. of days: 28/29 days")
   
# What I did was try to assign multiple items to one variable. The program didn't end up reading the variable properly and it gave no output. 
# I fixed this by putting all input possibilities into lists instead of assigning them to a variable:

# Separate the months into lists according to how many days there are in them.
months_with_31days = ["January", "March", "May", "July", "August", "October", "December"]
months_with_30days = ["April", "June", "September", "November"]
months_with_28_29days = ["February"] # Lists can contain only one item. I put February into its own list instead of just as a variable for readability and efficiency.

input_from_user = input("Input the name of Month: ") # Display "Input the name of Month" and retrieve user input as variable input_from_user

if input_from_user in months_with_31days:
   print("No. of days: 31 days")
elif input_from_user in months_with_30days:
   print("No. of days: 30 days")
elif input_from_user in months_with_28_29days:
   print("No. of days: 28/29 days")
# This checks which list the input is a part of. Since all input possibilities are accounted for in the lists, I can ask the program to display however many days are in that month according to which list I have put it in.
