#mayar muhammad elsayed muhammad
#2nd laps
#1)
list=[]
for trails in range(3):
 item=input("enter an item")
 list.append(item)
 asc=sorted(list)
 dsc=sorted(list, reverse=True)
print(asc)
print(dsc)
#2)
list2=[]
number=int(input("enter a number"))
for i in range (1,number+1):
 row=[]
for j in range (1,number+1):
  multp=i*j
  row.append(multp)  
  list2.append(row)  
print(f"{number}:{list2}")

#3)
for trails in range (4):
 username=input("enter a name please: ")

 if not username or username==" ":
    print("please enter a username not empty value: ") 

 elif username.isdigit():
     input("please enter a name not a number ")
 else:
         email=input("please enter your email: ")
         break
print(f"user:{username},email:{email}")

