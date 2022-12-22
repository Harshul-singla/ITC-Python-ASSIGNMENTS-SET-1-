#qn6

conti = True
list_students = {}
while conti: 
    list_students[int(input("Enter SID : "))] = ' '.join(input("Enter name : ").split()) #computes name first then sid
    yn = input("Add more entries(Y/N): ").lower()
    if yn == 'y' : conti = True
    elif yn == 'n' : conti = False
    else: raise RuntimeError("Please enter Y or N only")

#print(list_students.items())
for i in list_students.keys():print("SID :", i, "Name :", list_students[i])

#key is the custom function to sort the given list by (here .items()
#dict.items() has keys on 0th index and items on 1st, thus the (lambda) function gives the same as the sorting key
list_sorted_nam = sorted(list_students.items(), key = lambda pq:pq[1])
print(list_sorted_nam)
list_sorted_sid = sorted(list_students.items(), key = lambda pq:pq[0])
print(list_sorted_sid)

sid = int(input("Enter SID of registered student: "))
if sid in list_students.keys() : print("Name: ", list_students[sid])
else : print("Given SID not registered")

    
