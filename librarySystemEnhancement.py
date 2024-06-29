library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def lookupBook(title, author):
    titles = []
    authors = []
    for book in library:
        titles.append(book[0])
        authors.append(book[1])
    found_Title = True if title in titles else False
    index = titles.index(title) if found_Title == True else -1
    # This allows for duplicate titles and duplicate authors, but not duplicate titles *with* duplicate authors
    found_Author = index if authors[index] == author else -1
    return found_Author

def addBook(title, author):
    found = lookupBook(title, author)
    if found == -1:
        library.append((title, author))
    else:
        print(f"{title} by {author} is already in library.")

addBook("1984", "George Orwell")
addBook("1984", "Bob")
addBook("An Encyclopedia of Fairies", "Katherine Briggs")
print(library)