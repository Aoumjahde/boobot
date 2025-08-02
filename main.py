from stats import get_book_text
from stats import sptlitingString
from stats import countChar
from stats import chars_dict_to_sorted_list

def main():
    textContent = get_book_text("books/frankenstein.txt")
    # sptlitingString(textContent)

    listCharactesr = countChar(textContent)
    chars_dict_to_sorted_list(listCharactesr)




main()