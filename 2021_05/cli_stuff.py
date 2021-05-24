def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

while True:
    answer = input()
    correct = 2
    if int(answer) == correct:
        print("Completed, have a nice day!")
        exit()
    elif answer != correct:
        print("Please, try again.")
     
    

def end():
    print('Congratulations, have a nice day!')