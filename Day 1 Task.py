#mayar muhammad elsayed muhammad
#1st lap
#1)
def vouls():
 string=input("please enter a srting")
 charcs="eaoui"
 for charc in charcs:
     count=string.count(charc)
     print(f"{charc}: {count}")

#2)
phrase=input("enter string")
target="i"
for location,charcter in enumerate(phrase):
    if target==charcter:
      print(f"{target}: found at location:{location}")

#3)
number=int(input("enter a number:"))
for i in range (1, number+1):
   for j in range (1, number+1):
       print(f"{i}*{j} :{"multiplication =", i*j }")
        
#4) 
height=int(input("enter a height:"))
for width in range (1, height+1): 
    hash=width
    top= height-width
    print(hash * '#', top * ' ')
 
