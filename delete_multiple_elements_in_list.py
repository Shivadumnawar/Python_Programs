'''  By using list comprehension, please write a program 
to print the list after removing the 0th, 2nd, 4th,6th
 numbers in [12,24,35,70,88,120,155]. Hints: Use list 
 comprehension to delete a bunch of element from a list.
 Use enumerate() to get (index, value) tuple  '''
 
list1= [12,24,35,70,88,120,155]
        
list2= [ y for x,y  in enumerate(list1) if x not in [0,2,4,6]]
print(list2)
