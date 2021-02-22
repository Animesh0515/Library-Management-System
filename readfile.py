def readfile():
    file=open("List of Books.txt","r")
    content=file.readlines()
    return content
    file.close()
