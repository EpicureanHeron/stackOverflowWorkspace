rule_seq = [['#1', '#2', '#3'],  ['#1', '#2', '#3']]

KG_seq = [['nationality', 'placeOfBirth', 'locatedIn'],
 ['nationality', 'hasFather', 'nationality']]

# unify_dict = 
# {'#1': ['nationality'],
#  '#2': ['placeOfBirth', 'hasFather'],
#  '#3': ['locatedIn', 'nationality']}

def dict_list(list1, list2):
    output_dict = {}
    for x in list1:
        print(x)

dict_list(rule_seq, KG_seq)