def get_book_text(filePath):
    with open(filePath, encoding="utf8") as f:
        file_contents = f.read()
        return file_contents

def sptlitingString (textContent):
    count = 0
    textSpliting = textContent.split()
    print(textSpliting)

    for word in textContent:
        count +=1
    print(f"{count} words found in the document")

def countChar(counting):
        charachterDict = dict()
        characterList = list(counting)

        for char in characterList:
                if char in charachterDict:
                    charachterDict[char] += 1
                else:
                       charachterDict[char] = 1
                
        print(charachterDict)

