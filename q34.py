# 34. What is the output of the following code fragment? Explain.
fout = open("output.txt", 'w')
fout.write("Hello, world!\n")
fout.write("How are you?")
fout.close()
# Wrong syntax: file("output.txt").read()

"""
output : 
Hello, world!
How are you?

"""