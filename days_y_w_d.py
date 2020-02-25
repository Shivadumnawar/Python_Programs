'''  Write a  program to convert days 
        into years, weeks and days.
'''
days= int(input("number of days :"))
year= days//365
days= days%365
weeks= days//7
days=days%7
num_of_days = days
print("number of years :",year)
print("number of weeks :",weeks)
print("number of days :",num_of_days)