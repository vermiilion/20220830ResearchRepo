### Activity 2: Convert a month name to a number of days.

```months_with_31days = ["January", "March", "May", "July", "August", "October", "December"]
months_with_30days = ["April", "June", "September", "November"]
months_with_28_29days = ["February"]

input_from_user = input("Input the name of Month: ")

if input_from_user in months_with_31days:
   print("No. of days: 31 days")
elif input_from_user in months_with_30days:
   print("No. of days: 30 days")
elif input_from_user in months_with_28_29days:
   print("No. of days: 28/29 days")```
