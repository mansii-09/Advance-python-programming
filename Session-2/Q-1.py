file = open("lyrics.txt","r")

print("Position before reading:", file.tell())

data = file.read(10)
print("First 10 characters:",data)

print("Position after reading:", file.tell())

file.close()