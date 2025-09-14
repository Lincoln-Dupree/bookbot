def book_num_words(book_contents):
    words_arr = book_contents.split()
    num_words = len(words_arr)
    return f'{num_words} words found in the document'