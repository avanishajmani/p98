def swappingFile():
    fname1 = input("enter the file name 1: ")
    fname2 = input("enter the file name 2: ")
    with open(fname1,"r") as a:
        data_a = a.read()
    with open(fname2,"r") as b:
        data_b = b.read()
    with open(fname1,"w") as a: 
        a.write(data_b)
    with open(fname2,"w") as b: 
        b.write(data_a)  
swappingFile()