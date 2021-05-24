days = ["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
# set variable answered to be false to facilitate while loop
answered = False

# check to see value of answered
while answered == False:


    userInput = input("What day of the week would you like to assign a event: ")
    lst = []
    input_words=userInput.lower().split()
    for word in input_words:
        if word in days:
            lst.append(word)
            print(word)
            # set answered to True boolean
            answered = True
            
    # only evaulated after reviewing all words, if True is not set, prompts user again and let's them know that their answer is not valid
    if answered == False:
         print("You typed days of week wrong! Try Again!")

