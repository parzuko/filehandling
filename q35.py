# 35. Write the output of the following code with justification if the contents of the file ABC.txt are:
#Welcome to Python Programming!
f1 = open("output.txt", "r")
size = len(f1.read())
print(size)
data = f1.read(5)
print(data)

"""
output:
26
Hello

"""