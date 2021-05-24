# Stack Overflow Link https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string


def get_unique_words(text):
    # converts all alphabetical characters to lower
    lower_text = text.lower()
    # splits string on space character 
    split_text = lower_text.split(' ')
    # sorts values in list 
    split_text.sort()
    # empty list to populate unique words
    results_list = []
    # iterate over the list
    for word in split_text:
        # check to see if value is already in results lists
        if word not in results_list:
            # append the word if it is unique
            results_list.append(word)
    print(results_list)
text = "The quick brown fox jumps over the lazy dog!"

get_unique_words(text)