dog_age = int(input("Input dog's age in human years: "))

if dog_age <= 2:
   human_age = dog_age * 10.5
   print (human_age)
elif dog_age > 2:
   human_age = ((dog_age-2)*4)+21
   print("Your dog's human age is" , (human_age))
