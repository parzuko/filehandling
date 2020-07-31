# 31. Write appropriate statements to do the following:
# (a) To open a file named “RESULT.DAT” for output.
# (b) To go to the end of the file at any time.

# Step 1 -> Writing/Creating a Binary file
import pickle
record = []
while True:
    roll_no = int(input("roll: "))
    name = input("name: ")
    data = [roll_no, name]
    record.append(data)
    choice = input("continue? ").upper()
    if "N" in choice:
        break

with open("result.dat", "wb") as f:
    pickle.dump(record, f)
    print("record addded :))")

# Step 2 : openig file and accessing specific locations within the file
with open("result.dat",'rb') as f:
    print(f"current location of the pointer is: {f.tell()}")
    file_content = f.read()
    print(f"final location of the file is: {f.tell()}")
    # one more way would be doing f.seek(2)