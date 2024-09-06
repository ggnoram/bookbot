def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = get_char_dict(text)
    
    print_report(book_path, num_words, char_dict)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def print_report(book_path, num_words, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"\n{num_words} words found in the document\n")
    
    sorted_list = char_dict_to_sorted_list(char_dict)
    for dict in sorted_list:
        char = dict["char"]
        num = dict["num"]
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {num} times")
    print("\n--- End of report ---")
    
def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    main()
