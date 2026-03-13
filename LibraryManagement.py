class Library:
    # books=["Java","Python","css","html"]
    books=[] 
    noOfBooks=0

    def addbook(self,bk):
        self.books.append(bk)

    def book(self):
        print(f"Books are : {self.books}")
        print(f"Total books available are : {len(self.books)}")

a=Library()

a.addbook("Harry potter")
a.addbook("Shades of peogen")
a.addbook("rich dad ,poor dad")

a.book()