def selectionsort(list):
     n=len(list)
     for i in range(n-1):
         min_index=i
         for j in range(i+1,n):
             if list[j]<list[min_index]:
                 min_index=j
         list[i],list[min_index]=list[min_index],list[i]
     return list
     
list=[30,10,40,7] 
print("selection sort= ", selectionsort(list))
    