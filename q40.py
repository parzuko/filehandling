# 40. Write a statement to open a binary file C:\Myfiles\Text1.txt in read and write mode by specifying for file
# path in two different formats.

#method 1

BASE_PATH = "C:/Myfiles/" 
file_name = input("enter name of file")

main_file = BASE_PATH+file_name

with open(f"{main_file}", 'r') as good_answer: