import Keepingin2dlist as k
import readfile as r
list=r.readfile()
list2=k.store_2dlist(list)
def input_user():
    print('''1.Do you want to borrow the books?
2.Do you want to return the book?
0.Exit''')
    user_input=int(input("Choose the option 1 or 2 or 0:"))
    return user_input
def choice_first():
    selection="yes"
    while selection=="yes":
        try:
            Book_No=int(input("Which book do you want to borrow??Please press S.No to borrow book or Press 0 to exit="))
            return Book_No
            selection="no"
        except Exception as e:
            print("Invalid Input")
def choice_third():
    print("Thank you for visiting")
        
def Book_no(SNO):
    if(SNO!=0):
        real_sno=SNO-1
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                if(real_sno==i and j==0):
                    Book_borrowed=list2[i][0]
                    Book_author=list2[i][1]
                        
    return Book_borrowed,Book_author

    

def quantity(SNO):
    real_sno=SNO-1
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if(real_sno==i and j==0):
                selection="yes"
                while selection=="yes":
                    try:
                        quantity=int(input("Enter quantity you want,Less than 2="))
                        selection="no"
                    except Exception as e:
                        print("Invalid Input")
                if(quantity>2):
                    print("Sorry you are allowed to borrow more than 2 books")
                    quantity=int(input("Enter quantity again,less than 2="))
                
                tot_quantity=float(list2[i][3].replace("$",""))
                tot_amount=tot_quantity*quantity
                return tot_amount,quantity


def user_name():
    user_name=input("Enter your full name:")
    return user_name
       
        
 
def print_bill_data(list2d,user_name,tot_amount,quantity):
    book = []
    for i in range(len(list2d)):
        if(list2d[i][0]==user_name):
            
            book.append(list2d[i][2])
            book.append(list2d[i][4])
            book.append(list2d[i][5])
            
    return book

def print_bill(data):
    print("\n\n")
    dash="-"*50
    print("Here is your Bill")
    print(dash,"\n","Book","\t\t\t\t","Quantity")
    print(dash)
    if(len(data)<=3):
        if(len(data[0])>15):
            print(data[0],"\t",data[1])
        else:
            print(data[0],"\t\t\t",data[1])
        print(dash,"\n","Total Amount:","\t\t\t",data[2])
    else:
        if(len(data[0])>15):
             print(data[0],"\t",data[1])
        else:
            print(data[0],"\t\t\t",data[1])
        if(len(data[3])>15):
            print(data[3],"\t",data[4])
        else:
            print(data[3],"\t\t\t",data[4])
        tot_amount=float(data[2])+float(data[5])
        print(dash,"\n","Total Amount:","\t\t\t",tot_amount)
    print(dash)
    
def reduce_quantity_list(list_,book_no,quantity):
    sno=book_no-1
    list_[sno][2]=int(list_[sno][2])-quantity
    list_[sno][2]=str(list_[sno][2])
    return list_
    
def add_quantity_list(list_1,quantity,book_name_return,index_position):
    real_index=index_position-1
    real_book_name=book_name_return[real_index]
    if(len(str(quantity))==1):
        for i in range(len(list_1)):
            if(book_name_return[real_index]==list_1[i][0]):
                list_1[i][2]=int(list_1[i][2])+quantity
                list_1[i][2]=str(list_1[i][2])
    else:
        for i in range(len(list_1)):
            if(book_name_return[real_index]==list_1[i][0]):
                quantity=int(quantity[real_index])
                list_1[i][2]=int(list_1[i][2])+quantity
                list_1[i][2]=str(list_1[i][2])
   
    return list_1,real_book_name,quantity
            
    
            
