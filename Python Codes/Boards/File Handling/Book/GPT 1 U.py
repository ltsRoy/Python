"""Data Analysis:
Write a Python program to read data from a CSV file 
named "sales.csv" containing sales data (Product Name, Quantity Sold, Price per Unit). 
Calculate the total revenue generated from each product and 
display the results sorted by revenue in descending order."""

import csv
with open("sales.csv","r") as fh:
    r=csv.reader(fh)
    sum=0
    for i in r:
        sum=int(i[1])*int(i[2])
        print("Revenue from ",i[0]," is: ",sum)
        
    
    