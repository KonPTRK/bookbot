from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            num = item["num"]
            print(f"{char}: {num}")

    print("============= END ===============")

main()