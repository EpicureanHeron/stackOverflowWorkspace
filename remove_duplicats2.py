text = "Conscious of its spiritual and moral heritage, the Union is founded on the indivisible, universal values of human dignity, freedom, equality and solidarity; it is based on the principles of democracy and the rule of law. It places the individual at the heart of its activities, by establishing the citizenship of the Union and by creating an area of freedom, security and justice."

words = []

def get_unique_words(text):
    # converts all alphabetical characters to lower
    lower_text = text.lower()
    # splits string on space character 
    split_text = lower_text.split(' ')

    # empty list to populate unique words
    results_list = []
    # iterate over the list
    for word in split_text:
        # check to see if value is already in results lists
        if word not in results_list:
            # append the word if it is unique
            results_list.append(word)
    return results_list

results = get_unique_words(text)

print(results)