file = open("intro myself.txt","r")
#print(file.readable())

#text = file.read()
#print(text)

#size = len(text)
#print(size)

#text = file.readlines()
#text = file.readlines()[0]
#print(text)

for line in file :
    print(line)

file.close()