
def display(list_2d):
    print("\t\t\t","  ","Welcome to the Library")
    print("\t\t\tHere are the list of the Books ","\n")
    dash='-'*95
    print(dash)
    print("S.NO\t\t","Book Available\t\t\t","Author\t\t\t","Quantity\t","Price")
    print(dash)
    for i in range(len(list_2d)):
        print(i+1,end="\t\t ")
        for j in range(len(list_2d[i])):
            if(len(list_2d[i][j])>22):
                 print(list_2d[i][j],end="\t ")
            elif(len(list_2d[i][j])>14 and len(list_2d[i][j])<22):
                print(list_2d[i][j],end="\t\t ")
            else:
                print(list_2d[i][j],end="\t\t ")
                if(j==0):
                    print(end="\t ")
   
                
        print("\n")
    print(dash)
   





