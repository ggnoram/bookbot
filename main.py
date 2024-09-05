def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    char_dict = get_char_dict(text)
    print(f"Count of each character in the document: {char_dict}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

if __name__ == "__main__":
    main()

