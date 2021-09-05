subject =["C","C++","Java","Python","Java","Java","Java"]

print(len(subject))

subject.append("BASIC")
print(subject)

subject.insert(2,"OS")
print(subject)

subject.remove("BASIC")
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)
'''
subject.pop()
subject.pop()
print(subject)

subject.clear()
print(subject)

subject1 = subject.copy()
print(subject)
'''
pos = subject.index("Java")
print(pos)

COUNT = subject.count("Java")
print(COUNT)