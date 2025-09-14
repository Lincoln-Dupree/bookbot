from stats import book_num_words



def main():
    print(book_num_words(get_book_text("./books/frankenstein.txt")))

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents
    


main()