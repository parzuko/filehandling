# Anant has been asked to display all the students who have scored less than 40 for Remedial Classes. Write
# a user-defined function to display all those students who have scored less than 40 from the binary file
# “Student.dat”.

# Assuming Student.dat is in the same folder and has format -> name, marks
import pickle
with open("student.dat",'r') as student_info:
    student_record = pickle.load(student_info)
    mark_parameter = 40
    for record in student_record:
        if record[1] < 40:
            print(record)
    print("thats all folks")