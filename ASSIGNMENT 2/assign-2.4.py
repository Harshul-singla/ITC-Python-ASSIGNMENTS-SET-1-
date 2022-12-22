x= int(input("1st No. \n>"))
y= int(input("2nd No. \n>"))
z= int(input("3rd No. \n>"))
p= 0
q= True 
 #print(a,b,c)
    if(x>y):
        p=x
        if(z>x):
            p=z
        elif(x==z):
            q= False
            print(x,z, " are greatest ")
    elif(y>x):
        p=y
        if(z>x):
            p=z
        elif(y==z):
            q= False
            print(y,z, " 2nd and 3rd Nos. are greatest numbers ")
    elif(x==y & x>z):
        q= False
        print(x,y, "1st and 2nd Nos. are greatest numbers")
    elif(x==y==z):
        print("All are equal")
        q= False
        
    if(q):
        print(p, "Is the greatest")