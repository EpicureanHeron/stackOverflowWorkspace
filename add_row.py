import csv



with open('test.csv') as f:
     reader = csv.reader(f)
     for row in reader:    
         print(row)     
         print(len(row))            
         if len(row) == 2:
             row.append(' ')
             print(row)
             
             


