


def best_conjugation(word):
    word = str(word)
    words = ''

    with open('programs/wordlist.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            if word.find(line) == True:
                words += line


    return words




if __name__ == "__main__":


    jeff = 'awesomeness'
    print(best_conjugation(jeff))


