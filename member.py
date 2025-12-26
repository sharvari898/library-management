class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


    def borrow(self,isbn):
        self.borrowed_books.append(isbn)
    def return_book(self,isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def list_borrowed_books(self):
        return self.borrowed_books


m1 = Member("Sharvari",1234)
m2 = Member("Gaurav",2311)
m3 = Member("sakshi",4555)