def binary_search(list,target):
         list=sorted(list)      # in built sort function 
         start=0
         end=len(list)-1
         while start<=end:
             mid=(start+end)//2
             if list[mid]==target:
                 print("search successful at position",mid)
                 break
             elif list[mid]<target:
                  start=mid+1
             else:
                  end=mid-1
         else:
             print("search unsuccessful:")
                   
array=['Vadodara','Indore','Mumbai','Pune','Surat']
binary_search(array,'Indore')