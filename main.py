from stats import get_num_words, get_num_char


def get_books_text(path_to_tile):
    with open(path_to_tile) as f:
        file_contents = f.read()
    return file_contents


# print(
#    get_num_words(get_books_text("books/frankenstein.txt")),
#    "words found in the document",
# )
print(get_num_char(get_books_text("books/frankenstein.txt")))
