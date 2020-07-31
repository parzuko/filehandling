# Write a program to add two more employees’ details to the file “emp.txt” already stored in disk.
import pickle

with open("emp.dat", 'ab') as file:
    for _ in range(2):
        id = int(input('enter emp id: '))
        name = input("enter emp name: ")
        employee = [name, id]
        pickle.dump(employee)
