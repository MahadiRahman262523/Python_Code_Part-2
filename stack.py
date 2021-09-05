books = []

books.append("learn C")
books.append("learn C++")
books.append("learn Java")
books.append("learn Python")

print(books)

books.pop()
print(books)
print("now the top book is :",books[-1])

books.pop()
print(books)
print("now the top book is :",books[-1])

books.pop()
print(books)
print("now the top book is :",books[-1])

books.pop()
if not books:
    print("no books left")