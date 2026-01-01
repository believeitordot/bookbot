import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionaries


def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    char_count = count_characters(text)
    for item in sort_dictionaries(char_count):
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['count']}")
    print("============= END ===============")
    return None

main()
