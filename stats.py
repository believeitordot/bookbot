def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["count"]

def sort_dictionaries(char_count):
    char_list = []
    char_item = {}

    for character, count in char_count.items():
        char_item = {"char": character, "count": count}
        char_list.append(char_item)


    char_list.sort(reverse=True, key=sort_on)
    
    return char_list