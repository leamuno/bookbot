def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_sorted_chars(chars_dict)
    for char in chars_sorted_list:
        print(f"The '{char['char']}' character was found {char['occurences']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["occurences"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    return chars

def get_sorted_chars(chars):
    sorted_list = []
    for char in chars:
        sorted_list.append({"char":char, "occurences":chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
