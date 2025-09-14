from stats import book_num_words
from stats import book_num_char
from stats import sort_dict

def main():
    # print(book_num_words(get_book_text("./books/frankenstein.txt")))
    # print(book_num_char(get_book_text("./books/frankenstein.txt")))
    # print(sort_dict(book_num_char(get_book_text("./books/frankenstein.txt"))))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(book_num_words(get_book_text("./books/frankenstein.txt")))
    print("--------- Character Count -------")
    for each in sort_dict(book_num_char(get_book_text("./books/frankenstein.txt"))): 
        print(f'{each[0]}: {each[1]}')

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents
    


main()