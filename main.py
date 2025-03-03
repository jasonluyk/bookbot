from stats import get_book_text
from stats import get_char_count
from stats import list_dict
import sys



def main():

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_book_text(sys.argv[1])
    print("--------- Character Count -------")
    char_list = get_char_count(sys.argv[1])
    final_list = list_dict(char_list)
    for char in final_list:
        print(f"{char['char']}: {char['count']}")

main()
