import Keepingin2dlist as k
global book_borrowed_return
book_borrowed_return=[]
global book_quantity_return
book_quantity_return=[]
def writefile(Book_borrowed,Book_author,user_name,tot_amount,date,quantity):
    file=open("Book_borrower.txt","a")
    file.write(user_name)
    file.write(",")
    file.write(str(date))
    file.write(",")
    file.write(Book_borrowed)
    file.write(",")
    file.write(Book_author)
    file.write(",")
    file.write(str(quantity))
    file.write(",")
    file.write(str(tot_amount))
    file.write("\n")
    file.close()
    return user_name



def readdata():
    f=open("Book_borrower.txt","r")
    content=f.readlines()
    list2d=k.store_2dlist(content)
    return list2d

   
def update_file(list_2d):
    file=open("List of books.txt","w")
    for i in range (len(list_2d)):
        for j in range(len(list_2d[i])):        
            file.write(str(list_2d[i][j]))
            if(j<3):
                file.write(",")
        file.write("\n")   
    return list_2d
    


def read_modifiy(quantity,book_name,index_position):
    real_index=index_position-1
    list=readdata()
    for i in range(len(list)):
        if(list[i][2]==book_name[real_index]):
            if(len(str(quantity))==1):
                list[i][4]=int(list[i][4])-quantity
           
            else:
                list[i][4]=int(list[i][4])-int(quantity[real_index])
    return list
def mod_borrowed_file(list):
    file=open("Book_borrower.txt","w")
    for i in range (len(list)):
        for j in range(len(list[i])):
            if(list[i][4]!=0):
                file.write(str(list[i][j]))
                if(j<5):
                    file.write(",")
        if(list[i][4]!=0):
            file.write("\n")   
def store_return_data(book_name,quantity):
    book_borrowed_return.append(book_name)    
    book_quantity_return.append(quantity)
    return book_borrowed_return,book_quantity_return
     
