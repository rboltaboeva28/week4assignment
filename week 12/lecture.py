file = open('filename.txt', "r")
content = file.read()
file.close()

file.read()
file.readline()
file.readlines()

file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()

file.open("data.txt", "r")
print(file.read(5))
print(file.tell())

file.seek(0)
print(file.read(5))
file.close()