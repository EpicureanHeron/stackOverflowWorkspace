x = ['bread','rice','butter','beans','pizza','lasagna','eggs']

criteria = lambda value:value[0]=='b'
     
c_list = list(filter(criteria,x))

print(c_list)