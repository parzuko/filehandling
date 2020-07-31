# 47. Create a CSV file “Groceries” to store information of different items existing in a shop. The information is
# to be stored w.r.t. each item code, name, price, qty. Write a program to accept the data from user and
# store it permanently in CSV file.

import csv
fields = ['item_code',"name","price","qty"]

with open("groceries.csv",'r+') as groc:
    line = []
    while True:
        item_code = int(input("code: "))
        name = input("enter name: ")
        price = int(input("Price: "))
        qty = int(input("qty: "))
        line.append([item_code, namem price, qty])
        choice = input("continue? ").lower()
        if 'n' in choice:
            break
    
    writer = csv.writer(groc)
    writer.writerow(fields)
    for each in line:
        writer.writerow(each)
    print("Done :)")
