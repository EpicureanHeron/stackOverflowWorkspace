
try:
    theAlphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet=input("Give me a number between 1 and 26: ")
    print(len(theAlphabet))
    print(theAlphabet[int(alphabet)-1])

except IndexError:
    print("Your number is out of range")
except: 
    print("Something else occurred")

