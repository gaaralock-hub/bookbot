def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_chars_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in chars_list:
        print(f"The {char["character"]} character was found {char["num"]} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha() == True:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_chars_list(chars_dict):
    list = []
    for key, val in chars_dict.items():
        list.append({"character": key, "num": val})
    return list

def sort_on(chars_list):
    return chars_list["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
