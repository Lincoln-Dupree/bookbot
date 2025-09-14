from collections import Counter

def book_num_words(book_contents):
    words_arr = book_contents.split()
    num_words = len(words_arr)
    return f'Found {num_words} total words'

# def book_num_char(book_contents):
#     lowercase_list = book_contents.lower()
#     char_list = list(lowercase_list)
#     default_count = 0
#     unique_dict = dict.fromkeys(char_list, default_count)
#     for char in char_list:
#         if char in unique_dict:
#             unique_dict[char] += 1

#     return unique_dict

def book_num_char(book_contents):
    return Counter(book_contents.lower())

def sort_dict(dict):
   return sorted(dict.items(), key=lambda item: item[1], reverse=True)

