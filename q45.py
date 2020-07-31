# 45. Write code to open the file in the previous question and print it in the following form:
# Name : <name> Phone: <phone number>

import csv
with open("contacts.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    hashmap = {}    
    for each in reader:
        hashmap['Name'] = each[0]
        hashmap['Phone'] = each[1]

    print(hashmap)