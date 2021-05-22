input = [("abc", 2), ("def", 7), ("abc", 6), ("ghi", 2), ("ghi", 5)]

output = []
first_tups = []

for tup in input:
    if tup[0] not in first_tups:
        output.append(tup)
        first_tups.append(tup[0])

print(output)