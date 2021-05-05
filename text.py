# Stack Overflow Link https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string


def get_unique_words(text):
    # converts all alphabetical characters to lower
    lower_text = text.lower()
    # splits string on space character 
    split_text = lower_text.split(' ')
    # sorts values in list 
    split_text.sort()
    
    print(split_text)

text = "The quick brown fox jumps over the lazy dog!"

get_unique_words(text)