import random

words = ['funny', 'funny']

def word_guess():
    random.shuffle(words)
    word = words[0]
    words.pop(0)

    print(word)
    l_count = 0
    for letter in word:
        l_count += 1

    # the hidden words are shown a '-'
    blank = '-' * l_count
    print(blank)

    guess = input("please guess a word  ")

    if guess in word:
        # a list of the position of all the specified letters in the word
        a = [i for i, letter in enumerate(word) if letter == guess]
        print(a)
        for num in a:
            print(num)
            blank.split('')
            blank[num] = guess
            print(blank)


word_guess()