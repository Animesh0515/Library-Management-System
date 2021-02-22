import display as d
import function_used as f
import working_with_file as w
import create_receipt as c
import Keepingin2dlist as k
import readfile as r
from datetime import date
list=r.readfile()
list1=k.store_2dlist(list)
today=date.today()
def borrow_book():
    loop=1
    selection="yes"
    while(selection.lower()=="yes" or selection.lower()=="y"):
        d.display(list1)
        SNO=f.choice_first()
        if(SNO==0):
            selection=="no"
            loop+=1
        if(loop==1):
            global user_name
            user_name=f.user_name()                
        Book_borrowed,Book_author=f.Book_no(SNO)
        print("The Book you borrowed is:",Book_borrowed)
        print("Author:",Book_author)
        Total_amount,Quantity=f.quantity(SNO)
        print("The total amount:",Total_amount)
        
        w.writefile(Book_borrowed,Book_author,user_name,Total_amount,today,Quantity)
        
        list2=w.readdata()
        book=f.print_bill_data(list2,user_name,Total_amount,Quantity)
        list3=f.reduce_quantity_list(list1,SNO,Quantity)
        list_2d=w.update_file(list3)
        list_2d=list1
        c.create_receipt(Book_borrowed,Book_author,user_name,Total_amount,today)
        if(loop==1):
            selection=input("Do you want to brorwor another book?y/n")
            loop+=1
           
        else:
            print("Sorry you cannot borrow more than 2 books")
            selection="no"
          
    if(selection.lower()=="no" or selection.lower()=="n"):
        print("Thank you for letting us serve you")
    elif(selection.lower()!="yes" or selection.lower()!="y" or selection.lower()!="no" or selection.lower()!="n"):
        print("Invalid Input")
    f.print_bill(book)
