"""Write a Python program that reads a text file named "data.txt" 
    containing a list of integers separated by commas. The program should 
    calculate and display the sum of all the integers in the file.

Ensure that your program handles the case where the file might not exist or 
if the file is empty. In such cases, your program should display an appropriate error message.

Your program should also be able to handle non-integer values in the file 
gracefully, ignoring them while calculating the sum.
"""

fh=open("data.txt","r")
a=fh.read()
n=""
sum=0
if len(a)==0:
    print("Empty FIle")
    exit
for i in a:
    if i.isdigit():
        n+=i
    if i==',':
        sum+=int(n)
        n=""
fh.close()


try:
    with open("data.txt", "r") as fh:
        content = fh.read().strip()
        if not content:
            print("File is empty.")
        else:
            numbers = content.split(",")
            total_sum = 0
            for number in numbers:
                try:
                    total_sum += int(number)
                except ValueError:
                    pass  # Ignore non-integer values
            print("Sum of integers:", total_sum)
except FileNotFoundError:
    print("File does not exist.")


