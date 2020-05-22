'''   Write a program that accepts a sentence and calculate
 the number of upper case letters and lower case letters.
 Suppose the following input is supplied to the program: 
     Hello world! Then, the output should be: UPPER CASE 1 
     LOWER CASE 9  '''
     
     
txt= input("enter a sentence :")

upper_case=0
lower_case=0
for i in txt:
    if i.isupper()== True:
        upper_case+=1
    elif i.islower()== True:
        lower_case+=1
    else:
        pass
        
print(" uppercase letters: ", upper_case)
print(" lowercase letters: ", lower_case)
