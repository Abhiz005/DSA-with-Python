def bubblesort(list):
     n=len(list)
     for j in range(n-1):
      for i in range(n-j-1):
           if list[i]>list[i+1]: 
               list[i],list[i+1]=list[i+1],list[i]
     return list

list=[30,10,40,60,50,90,50,7] 
print("Bubble sort= ", bubblesort(list))

def mbubblesort(list):
    n=len(list)
    for j in range(n-1):
     for i in range(n-j-1):
       swap=False
       if list[i]>list[i+1]:
            swap=True 
            list[i], list[i+1]=list[i+1], list[i]
     if not swap:
         break
    return list

print()
print("ModifiedBubble sort= ",mbubblesort(list))    