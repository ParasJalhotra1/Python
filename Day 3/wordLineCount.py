def countWords(fileName):
    words = 0
    chars = 0
    lines = 0

    with open('wordLineCount.txt', 'r') as file:
        for line in file:
            wordlist = line.split()
            lines += 1
            words += len(wordlist)
            chars += len(line)

    print ("Words: ", words)
    print ("Lines: ", lines)
    print ("Characters: ", chars)

if __name__ == '__main__':
    countWords('wordLineCount.txt')