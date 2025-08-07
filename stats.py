def get_num_words(books):
    return len(books.split())


def get_num_char(books):
    books = books.lower()
    bookl = books.split()
    charcount = dict()
    for book in bookl:
        for char in book:
            if char not in charcount:
                charcount[char] = 1
            else:
                charcount[char] += 1

    return charcount
