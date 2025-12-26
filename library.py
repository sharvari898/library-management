from books import Books
from member import Member
import json
class Library:
    def __init__(self):
        self.books = {}
        self.member = {}
        self.load_books()

    def add_book(self,isbn,book):
        try:
            if isbn not in self.books:
                self.books[isbn] = book
                self.json_book.append(self.books)
                return "added successfully"
            else:
                return "already exists"
        except Exception as e:
            print("Exception occured while adding books",e)
    def remove_book(self,isbn):
        try:
            if isbn in self.books:
                self.books.pop(isbn)
                return "removed successfully"
            else:
                return "already exists"
        except Exception as e:
            print("Exception occured while adding books", e)

    def register_member(self,member_id,member_name):
        try:
            if member_id in self.member:
                self.json_member.append(self.member)
                return "member already exists"

            else:
                self.member[member_id] = member_name
                return f"member {member_name} registered successfully"
        except Exception as e:
            return f"exception occured {e}"
    def borrow_book(self,member_id,isbn):
        if isbn not in self.books:
            return "Book not found"
        if member_id not  in self.member:
            return "member is invalid"
        book = self.books[isbn]
        if not book.isavailble:
            return "book already borrowed"
        member = self.member[member_id]
        member.borrow()

    def load_books(self):
        try:
            with open("books.json", "r") as f:
                data = json.load(f)
                for isbn, book_data in data.items():
                    book = Books(
                        book_data["title"],
                        book_data["author"],
                        int(isbn)
                    )
                    book.isavailable = book_data["isavailable"]
                    self.books[int(isbn)] = book
        except FileNotFoundError:
            pass

    def return_book(self,member_id,isbn,book):
        self.books[isbn] = book
    def list_available(self):
        return self.books

b1 = Books("The Great Gatsby","F. Scott Fitzgerald",2341)
b2 = Books("Animal Farm","George Orwell",1211)
b3 = Books("Alice in Wonderland","Lewis Carroll",2555)
m1 = Member("Sharvari",1234)
m2 = Member("Gaurav",2311)
m3 = Member("sakshi",4555)
l = Library()

print(l.add_book(b1.isbn, b1.title))

print(l.add_book(b2.isbn, b2.title))

print(l.add_book(b3.isbn, b3.title))

l.list_available()
print(l.register_member(m2.member_id,m2.name))
print(l.register_member(m3.member_id,m3.name))
print(l.register_member(m1.member_id,m1.name))


print(l.borrow_book(m2.member_id,b1.title))


