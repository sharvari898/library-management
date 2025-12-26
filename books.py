class Books:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isavailable = True
        self.isbn = isbn

    def __str__(self):
        return f"title : {self.title} author : {self.author}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "isavailable": self.isavailable
        }


b1 = Books("The Great Gatsby","F. Scott Fitzgerald",2341)
b2 = Books("Animal Farm","George Orwell",1211)
b3 = Books("Alice in Wonderland","Lewis Carroll",2555)

print(b1)


