import pickle
list1, list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10], []
for i in list1:
    if (i%2==0 and i%4==0):
        list2.append(i)
f = open("bin.dat","wb")
pickle.dump(list2, f)
f.close()
f = open("bin.dat", "rb")
data = pickle.load(f)
f.close()
for i in data:
    print(i)

"""
output:
4
8

"""