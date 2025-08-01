from stats import get_num_words


def get_book_text(filePath):
    with open(filePath, encoding="utf8") as f:
        file_contents = f.read()
        return file_contents

def sptlitingString (textContent):
    textSpliting = textContent.split()
    print(textSpliting)


def main():
    textContent = get_book_text("books/frankenstein.txt")
    sptlitingString(textContent)

main()