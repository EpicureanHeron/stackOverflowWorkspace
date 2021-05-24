from bs4 import BeautifulSoup

def search():                                                                                                                                             
    get_inp_cert = inp_cert.get(1.0, "end-1c")                                                                                                            
    newname=get_inp_cert.replace('-', '').strip()                                                                                                         
    url = 'https://google.com'                                                                                               
    r = requests.get(url, allow_redirects=False)                                                                                                          
    soup = BeautifulSoup(r.content, 'lxml')                                                                                                               
                                                                                                                                                          
    for item in newname.split():                                                                                                                          
        words = soup.find(text=lambda text: text and item in text)                                                                                        
        if((words) == None):                                                                                                                              
            btnget = Button(mainwind, text="Get", command=lambda: getgen(item))                                                             
            btnget.pack(side=BOTTOM)                                                                                                                      
            lbl = Label(mainwind, text="\n\nstat " + item + " !!!")                                                                        
            lbl.pack(side=BOTTOM)                                                                                                                         
        else:                                                                                                                                             
            lbl = Label(mainwind,text="\n\nstat dont " + item + " !!!\n\n\n"+'Url: {}\ncontem {} ocorrencias: {}'.format(url, len(words), item))    
            lbl.pack(side=BOTTOM)    

search()