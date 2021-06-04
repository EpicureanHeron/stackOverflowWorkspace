

def opt_b_private():
    for row in data_file:
        num_opt_b = row[3:4]
    length_opt_b = len(num_opt_b)
    sum_opt_b = sum(num_opt_b) 
    average_opt_b = sum_opt_b / length_opt_b
    print(average_opt_b)
    
opt_b_private()
