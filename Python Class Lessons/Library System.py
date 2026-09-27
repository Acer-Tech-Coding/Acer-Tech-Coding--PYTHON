class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.fine_per_day = 2

    def borrow(self):
        self.is_borrowed = True
        print(f'You borrowed "{self.title}" by {self.author}.')

    def return_book(self, days_late=0):
        self.is_borrowed = False
        print(f'You returned "{self.title}" by {self.author}.')
        if days_late > 0:
            fine = days_late * self.fine_per_day
            print(f'Your fine is ${fine} for {days_late} overdue day(s).')
        else:
            print("No fine. The book was returned on time.")


book1 = Book("Charlotte's Web", "E. B. White")
book2 = Book("Matilda", "Roald Dahl")
book3 = Book("The Jungle Book", "Rudyard Kipling")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book(days_late=3)
book3.return_book()