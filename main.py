from stats import get_book_text
from stats import sptlitingString
from stats import countChar


def main():
    textContent = get_book_text("books/frankenstein.txt")
    # sptlitingString(textContent)

    countChar(textContent)



main()