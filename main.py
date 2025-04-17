from stats import get_num_words, get_chars_dict, get_sorted_lod
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
#    print(chars_dict)
    print("--------- Character Count -------")
    sorted_lod = get_sorted_lod(chars_dict)
    #print(f"Sorted list of dictionaries: {sorted_lod}")
    for i in sorted_lod:
        print(f"{i['char']}: {i['count']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()
main()
