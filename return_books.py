import working_with_file as w
import function_used as f
import Keepingin2dlist as k
import readfile as r
global list1
list=r.readfile()
def return_book():
    list1=k.store_2dlist(list)
    loop=1
    selection="yes"
    while(selection.lower()=="yes" or selection.lower()=="y"):
        list2=w.readdata()
        if(loop==1):
            user_name=input("Enter your name:")
            loop+=1
        book_borrowed2_return=[]
        book_author2_return=[]
        book_quantity2_return=[]
        for i in range(len(list2)):
            if(list2[i][0]==user_name):
                book_borrowed2_return.append(list2[i][2])
                book_author2_return.append(list2[i][3])
                book_quantity2_return.append(list2[i][4])
            elif(i==0 and list2[i][0]!=user_name):
                print("You have not borrowed any book recently")
                selection="no"
   
        if(len(book_borrowed2_return)>1):
            print("Books you borrowed:\n"+"1."+book_borrowed2_return[0]+"\n2."+book_borrowed2_return[1])
            print("Authors of the book:\n"+"1."+book_author2_return[0]+"\n2."+book_author2_return[1])
            print("Quantity of books borrowed:\n"+"1."+book_quantity2_return[0]+"\n2."+book_quantity2_return[1])
        elif(len(book_borrowed2_return)==1):
             print("Books you borrowed:\n"+"1."+book_borrowed2_return[0])
             print("Authors of the book:\n"+"1."+book_author2_return[0])
             print("Quantity of books borrowed:\n"+"1."+book_quantity2_return[0])
        if(len(book_quantity2_return)>=1):
            selection="yes"
            while selection=="yes":
                try:
                    book_no_return=int(input("Which book do you want to return.Please enter no(1or2) to select the book:"))
                    selection="no"
                except Exception as e:
                        print("Invalid Input")
        borrow_list=w.readdata()
        if(book_no_return==1):
            if(int(book_quantity2_return[0])>1):
                selection="yes"
                while selection=="yes":
                    try:
                        quantity_return=int(input("How many books do you want to return:"))
                        selection="no"
                    except Exception as e:
                        print("Invalid Input")
                list_1,book_name,quantity_1=f.add_quantity_list(list1,quantity_return,book_borrowed2_return,book_no_return)
                list1=w.update_file(list_1)
                list_2=w.read_modifiy(quantity_return,book_borrowed2_return,book_no_return)
                w.mod_borrowed_file(list_2)
                return_book_borrowed,return_book_quantity=w.store_return_data(book_name,quantity_1)
               
                print("Book has been returned succesfully")
            else:
                list_1,book_name,quantity_1=f.add_quantity_list(list1,book_quantity2_return,book_borrowed2_return,book_no_return)
                list1=w.update_file(list_1)
                list_2=w.read_modifiy(book_quantity2_return,book_borrowed2_return,book_no_return)
                w.mod_borrowed_file(list_2)
                w.store_return_data(book_name,quantity_1)
                print("Book has been returned succesfully")
        if(book_no_return==2):
            if(int(book_quantity2_return[1])>1):
                selection="yes"
                while selection=="yes":
                    try:
                        quantity_return=int(input("How many books do you want to return:"))
                        selection="no"
                    except Exception as e:
                        print("Invalid Input")   
                list_1,book_name,quantity_1=f.add_quantity_list(list1,quantity_return,book_borrowed2_return,book_no_return)
                list1=w.update_file(list_1)
                list_2=w.read_modifiy(quantity_return,book_borrowed2_return,book_no_return)
                w.mod_borrowed_file(list_2)
                w.store_return_data(book_name,quantity_1)
                print("Book has been returned succesfully")
            else:
                list_1,book_name,quantity_1=f.add_quantity_list(list1,book_quantity2_return,book_borrowed2_return,book_no_return)
                list1=w.update_file(list_1)
                list_2=w.read_modifiy(book_quantity2_return,book_borrowed2_return,book_no_return)
                w.mod_borrowed_file(list_2)
                w.store_return_data(book_name,quantity_1)
                print("Book has been returned succesfully")
        
        if(len(book_quantity2_return)>1):
            selection=input("Do you want to return another book")
        else:
            print("There are no more books to return")
            selection="no"
    if(selection.lower()=="no" or selection.lower()=="n"):
        print("Thank you for letting us serve you")
    #elif(selection.lower()!="yes" or selection.lower()!="y" or selection.lower()!="no" or selection.lower()!="n"):
        #print("Invalid Input")
    
