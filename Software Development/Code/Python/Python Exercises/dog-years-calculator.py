# Activity 1 Calculate a dog’s age in dog years.
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years. 

dog_age = int(input("Input dog's age in human years: "))

if dog_age <= 2:
   human_age = dog_age * 10.5
   print (human_age)
elif dog_age > 2:
   human_age = ((dog_age-2)*4)+21
   print("Your dog's human age is" , (human_age))
