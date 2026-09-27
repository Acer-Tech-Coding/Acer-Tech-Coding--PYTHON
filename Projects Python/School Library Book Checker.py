book_names = ["The Hobbit", "1984", "Pride and Prejudice", "The Great Gatsby"]
copy_counts = [3, 0, 5, 2]
late_fees = [1.00, 1.50, 0.75, 2.00]

library = dict(zip(book_names, copy_counts))
print("Current Library Inventory:", library)

available_books = {book: copies for book, copies in library.items() if copies > 0}
print("Available Books:", available_books)

chosen_book = input("Enter the book you want to borrow: ").strip()

if chosen_book not in library or library[chosen_book] == 0:
    print(f"Sorry, {chosen_book} is unavailable.")
    raise SystemExit

updated_late_fees = list(map(lambda fee: fee + 1, late_fees))
late_fee_by_book = dict(zip(book_names, updated_late_fees))
print("Updated late fees:", late_fee_by_book)

library[chosen_book] -= 1
print(f"You borrowed {chosen_book}.")
print(f"Late fee for {chosen_book}: ${late_fee_by_book[chosen_book]:.2f}")
print("Updated Library Inventory:", library)