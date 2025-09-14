import sys
from stats import book_num_words
from stats import book_num_char
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    # print(book_num_words(get_book_text("./books/frankenstein.txt")))
    # print(book_num_char(get_book_text("./books/frankenstein.txt")))
    # print(sort_dict(book_num_char(get_book_text("./books/frankenstein.txt"))))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(book_num_words(get_book_text(sys.argv[1])))
    print("--------- Character Count -------")
    for each in sort_dict(book_num_char(get_book_text(sys.argv[1]))): 
        print(f'{each[0]}: {each[1]}')

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents
    


main()