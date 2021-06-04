import numpy as np

mammal = ["monkey","dog","cat"]
amphibian = ["frog","toad","salamanders"]
aquatic = ["fish","eel","whale"]

animal_list = [mammal, amphibian, aquatic]


animal_list.append(['eagle'])

print(animal_list)

print(animal_list[2][2])

np_animal_list = np.array(animal_list)

print(np_animal_list[2][2])