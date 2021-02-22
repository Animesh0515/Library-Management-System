import borrow_books as b
import return_books as r1
import function_used as f
selection="yes"
while(selection=="yes"):
    try:
        user_selection=f.input_user()
        selection="no"
        if(user_selection==1):
            b.borrow_book()
            selection="no"
        elif(user_selection==2):
            r1.return_book()
            selection="no"
        elif(user_selection==0):
            f.choice_third()
            selection="no"
    except Exception as e:
        print("Invalid Input")
    
    

        

    
