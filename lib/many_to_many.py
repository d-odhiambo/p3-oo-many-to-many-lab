class Author:
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts related to this author"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return all books this author has contracts for"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties across all contracts"""
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts related to this book"""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return all authors related to this book via contracts"""
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # type validation
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match the given date"""
        return [c for c in cls.all if c.date == date]