def store_2dlist(list):
    list_2d=[]
    for i in range(len(list)):
        list_2d.append(list[i].replace("\n","").split(","))
    return list_2d
    
