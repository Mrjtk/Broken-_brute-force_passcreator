try:
    p=str(input("Enter the location of the password file :-"))
    a=eval(input("Enter what you wannt to add between :-"))
    l=str(input("Enter output file name:-"))
    f=open(l,"w+")
    b=open("pass.txt","r")
    d=b.read().splitlines()
    print(d)
    for i in d:
         f.write(i)
         f.write("\n")
         f.write(a)
         f.write("\n")
    f.close()
    b.close()
    print("All mixed password are stored in "+l)
except:
    print("Aborting !")