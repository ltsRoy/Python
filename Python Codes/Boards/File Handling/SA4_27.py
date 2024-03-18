"""Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code 
and the next three numbers.
 e.g. 017-555-1212 is a legal input.
 Display if the phone number entered is invalid format or not and display if the phone number is valid or not
"""


a=input("Enter no: ")
if len(a)>=8 and a[3]==a[7]=='-':
    print("LEGAL")
else:
    print("NAH MAN")
    
"sda"

"""
The string "sda" you mentioned isn't causing 
any error because it's a string literal enclosed 
within double quotes, which is perfectly valid Python syntax. 
Python allows you to write string literals without assigning 
them to variables or using them in any expression without causing an error. 
The interpreter simply evaluates the string and moves on.
    """