def linear_search(list,target):
     for x in list:
         if x==target:
             print("Search successful:")
             break
     else:
         print("search unsuccessful:")

array=['Vadodara','Indore','Mumbai','Pune','Surat']
linear_search(array,'Indore')   # we are searching 'Indore' in the list