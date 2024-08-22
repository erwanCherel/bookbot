def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    characters_count = get_count_characters(text)
    list_dicts = get_list_dicts(characters_count)
    list_dicts.sort(key=sort_on, reverse=True)

    for item in list_dicts:
        print(f"The '{item['character']}' character was found {
              item['occurences']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_characters(text):
    dict_count = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if not character in dict_count:
                dict_count[character] = 1
            else:
                dict_count[character] += 1
    return dict_count


def get_list_dicts(dictionary):
    return [{"character": key, "occurences": value} for key, value in dictionary.items()]


def sort_on(dict):
    return dict["occurences"]


main()
