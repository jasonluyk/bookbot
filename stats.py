def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    split_words = file_contents.split()
    num_words = 0
    for word in split_words:
        num_words += 1
    print(f"Found {num_words} total words")

def get_char_count(file):
    with open(file) as f:
        contents = f.read()
    split_words = contents.lower().split()
    char_count = {}
    for word in split_words:
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
    return char_count



def list_dict(char_count_dict):
    count_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            count_list.append({"char": char, "count": count})

    def dict_list(dict):
        return dict["count"]

    count_list.sort(reverse=True, key=dict_list)

    return count_list
