from stats import get_num_words, get_num_char, dict_sort


def get_books_text(path_to_tile):
    with open(path_to_tile) as f:
        file_contents = f.read()
    return file_contents


# print(get_num_char(get_books_text("books/frankenstein.txt")))
bookloc = "books/frankenstein.txt"
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(
    "Found",
    get_num_words(get_books_text("books/frankenstein.txt")),
    "total words",
)
print("--------- Character Count -------")
sorteddict = dict_sort(get_num_char(get_books_text("books/frankenstein.txt")))
for item in sorteddict:
    if item["char"].isalpha():
        print(item["char"], ": ", item["num"], sep="")
print("============= END ===============")
