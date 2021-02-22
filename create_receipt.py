global total_book_borrowed
total_book_borrowed=[]
global total_book_author
total_book_author=[]
def create_receipt(Book_borrowed,Book_author,user_name,tot_amount,date):
    topbar = "$" * 40 + "\n\n"
    total_book_borrowed.append(Book_borrowed)
    total_book_author.append(Book_author)
    if(len(total_book_borrowed)==2):
        string ="Username : "+user_name+"\nBook Name: "+total_book_borrowed[0]+","+total_book_borrowed[1]+"\nAuthor : "+total_book_author[0]+","+total_book_author[1]+"\n"
    else:
        string ="Username : "+user_name+"\nBook Name: "+total_book_borrowed[0]+"\nAuthor : "+total_book_author[0]+"\n"
    string =string+"Borrowed Date:"+str(date)+"\nTotal Price : "+str(tot_amount)+"\n\n"
    bottombar=topbar
    complete_string =topbar+string+bottombar
    if(len(total_book_borrowed)>1):
        file=open(user_name+".txt","a")
        file.write(complete_string)          
