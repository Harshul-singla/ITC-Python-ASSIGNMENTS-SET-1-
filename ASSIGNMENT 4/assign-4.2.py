a=int(input("enter the year"))

if a%4==0:
    
    if a%100==0 and a%400!=0:
        print("not a leap year")
        
    else:
        print("leap year")

if a%4!=0:    
    print("not a leap year")