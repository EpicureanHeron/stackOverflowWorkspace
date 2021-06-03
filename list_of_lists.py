import numpy as np

mammal = ["monkey","dog","cat"]
amphibian = ["frog","toad","salamanders"]
aquatic = ["fish","eel","whale"]

animal_list = [mammal, amphibian, aquatic]

list_of_lists = [animal_list[x] for x in range(0, len(animal_list))]

list_of_lists.append(['eagle'])

print(list_of_lists)

print(list_of_lists[2][2])