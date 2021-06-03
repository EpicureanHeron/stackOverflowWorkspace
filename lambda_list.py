x = ['bread','rice','butter','beans','pizza','lasagna','eggs']

criteria = lambda value:value[0]=='b'
     
c_list = list(filter(criteria,x))

# result = list(filter(lambda x: x!='t' , inp_list))
print(c_list)