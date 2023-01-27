import random

i=1
while (i<=10):
    R1= random.randint(0,9)
    print(R1)
    R2= random.randint(0,9)  
    print(R2)


    print("Question", R1 ,"*", R2,"=" )
    A1= int(input("Answer 1"))

    if A1==R1*R2:
      print("RIGHT!")
    
    else:
       print("The answer is WRONG, the correct answer is", R1*R2)
       
    i=i+1



