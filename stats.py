def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(char_dict):
    return char_dict["num"]

def sort_characters(char_counts_dict):
    char_list = []
    for char, num in char_counts_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
