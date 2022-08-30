i = 0
while i < 3:
    user_input = input("Enter two integers: ")
    #print(user_input)
    index_of_comma = user_input.find(",")
    #print(index_of_comma)
    number_in_string1 = (int(user_input[0:index_of_comma]))
    #print(number_in_string1)
    number_in_string2 = (int(user_input[index_of_comma+1:]))
    #print(number_in_string2)
    answer = 0
    if (number_in_string1%2 == 0 and number_in_string2%2 == 0) or (number_in_string1%3 == 0 and number_in_string2%3 == 0) :
        answer = number_in_string1 * number_in_string2
        #print("Both Numbers are divisible by 2 or 3")
    else:
        answer = number_in_string1 + number_in_string2
        #print("Both numbers isnt divisible by 2 or 3")
    print(answer,"\n")
    i+=1
