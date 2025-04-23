import random

def linearSearch(li,element):
    for x in range(len(li)):
        if li[x]==element:
            return x
       
    return -1

def randlist(n):
    li=[]
    for x in range(n):
        li.append(random.randrange(0,n))

    return li

li=randlist(100)
result=linearSearch(li,23)
if result==-1:
    print("The element was not found in the list")
else:
    print("The element was found in",result+1,"'th position")    
print(li)