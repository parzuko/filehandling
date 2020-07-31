# 39. Given a binary file “STUDENT.DAT”, containing records of the following type:
# [S_Admno, S_Name, Percentage]
# Where these three values are:
# S_Admno – Admission Number of student (string)
# S_Name – Name of student (string)
# Percentage – Marks percentage of student (float)
# Write a function in Python that would read contents of the file “STUDENT.DAT” and display the details of
# those students whose percentage is above 75.

import pickle
def read_file():
    with open("student.dat",'wb+') as f:
        info = pickle.load(f)
        answer =[]
        for details in info:
            if details[2] >75:
                answer.append(details)
    
    return answer

def main():
    read_file()

if __name__ == "__main__":
    main()