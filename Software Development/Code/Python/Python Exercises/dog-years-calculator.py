# Activity 1 Calculate a dog’s age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years. 

# This was the first piece of code I've ever written and it was the only exercise I didn't have too much trouble with, other than getting used to the syntax and figuring out the algorithm for claculating the years, since I was already familiar with the concept of "if" and "else" and "print" from Scratch. 

dog_age = int(input("Input dog's age in human years: ")) # Display "Input dog's age in human years" and retrieve user input as an integer into variable dog_age

if dog_age <= 2:
   human_age = dog_age * 10.5 # Because each year of the first two years of the dog's age will equal to 10.5 human years, human_age can be simply calculated by multiplying the input by 10.5, as long as the input <=2
   print ("Your dog's human age is" , (human_age)) # Display the dog's human age 
elif dog_age > 2: # If the dog age is > 2, a different algorithm is needed to find the variable human_age
   human_age = ((dog_age-2)*4)+21 # Since every year after 
   print("Your dog's human age is" , (human_age))
   
# In the middle of writing my comment explanations, I realised an error with my variables. the variable dog_age should have been named "human_age" since the input is the dog's age in HUMAN YEARS. The variable I'm trying to calculate should be "dog_age" since I am trying to convert human years to dog years. This can be solved by just swapping the variable names. I got confused with what I was trying to calculate and made an error with the end output "Your dog's human age is (human_age)".

human_age = int(input("Input dog's age in human years: "))

if human_age <= 2:
   dog_age = human_age * 10.5
   print (dog_age)
elif human_age > 2:
   dog_age = ((human_age-2)*4)+21 # Take away 2 years from the human age and multiply the total by 4. Since the first two human years of a dog's age are equivalent to 10.5 human years, not 4, we will account for these years separately. The two years in human years that aren't accounted for yet are equal to 21 dog years, so we add 21 to the total.
   print("Your dog's dog age is" , (dog_age)) 
