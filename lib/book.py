class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("title must be a string")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")  # ✅ just prints

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  # ✅ prints


# ---------------------------
# Example usage / test section
# ---------------------------
if __name__ == "__main__":
    # Create a Book instance
    my_book = Book("Python Basics", 350)

    # Print details
    print("Title:", my_book.title)
    print("Page Count:", my_book.page_count)

    # Use the turn_page method
    my_book.turn_page()

    # Try invalid input for page_count
    my_book.page_count = "three hundred fifty"  # will trigger validation print
