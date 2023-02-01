# Name: Tarek Alakkad
# Date of last edit: 2023-01-31 at 6:31 PM
# NOTE: for context regarding the program, take a look at README file


import sys
import re


class concord:

    #
    # BRIEF: constructor takes two string parameters - the input file
    # name, and the output filename. However, if the input filename is
    # 'None', then input is to be obtained from 'stdin'; if the output
    # is 'None', not to be generated directly to the console.
    #
    # PARAMETERS: input file (string), output file (string)
    #
    # RETURN: None (nothing). However, if an output filename is provided,
    # then the output from full_concordance is written to the given file.
    #
    def __init__(self, input=None, output=None):

        self.input = input
        self.output = output

        if output != None:
            self.__writeOutput()

        #
    # BRIEF: takes in an instance of concord object and returns the
    # concordance output as demonstrated in README.md.
    #
    # PARAMETERS: instance of concord object
    #
    # RETURN: list of strings corresponding to the output lines required
    # and as demonstrated in README.md
    #
    def full_concordance(self):
        allOfFile = self.__readFile()

        version = concord.__versionCheck(allOfFile)
        if version != []:
            return version

        exclusion_words = concord.__getExclusionWords(allOfFile)

        sentences = concord.__getSentences(allOfFile)

        sentences_copy = sentences

        indexed_words = concord.__getIndexedWords(exclusion_words, sentences)
        indexed_words.sort(key=lambda x: x.lower())

        concorded_lines = concord.__getConcordanceLines(
            indexed_words, sentences_copy)

        return concorded_lines

    #
    # BRIEF: takes in an instance of concord class and returns a list of
    # the contents of the file passed in.
    #
    # PARAMETERS: self (instance of concord class)
    #
    # RETURN: list of strings containing each line of file
    #
    def __readFile(self):
        fileI = []

        if self.input == None:
            txtFile = sys.stdin
            for line in txtFile:
                fileI.append(line)
        else:
            txtFile = open(self.input, "r")
            for line in txtFile:
                fileI.append(line)
            txtFile.close()

        return fileI

    #
    # BRIEF: takes in an instance of concord class and writes the
    # desired output into an output file provided as an argument.
    #
    # PARAMETERS: self (instance of concord class)
    #
    # RETURN: void (nothing), but the provided file now contains
    # desired output
    #
    def __writeOutput(self):
        txtFile = open(self.output, "w")

        output = self.full_concordance()

        for i in range(len(output)):
            txtFile.write(output[i] + '\n')

    #
    # BRIEF: takes in a list that contains the contents of input file
    # and returns a string containing the first line of the input file.
    # The first line contains the version number of said file.
    #
    # PARAMETERS: contents of input file (as a list)
    #
    # RETURN: string containing version number
    #
    def __versionCheck(fileI):
        version = []
        versionNum = fileI[0]

        if versionNum == '1':
            temp = "Input is version 1, concord4.py expected version 2"
            version.append(temp)

        return version

    #
    # BRIEF: takes in a list containing the contents of input file and
    # returns an integers that holds the end index of exclusion words
    # in the file. The end of exclusion words is marked by """".
    #
    # PARAMETERS: contents of input file (as a list)
    #
    # RETURN: end index of exclusion (as an int)
    #
    def __getQuotesIndex(allFile):
        index = 0

        for i in range(2, len(allFile)):
            quotes = re.search(allFile[i], "\"\"\"\"\n")
            if quotes:
                index = i
                break
        return index

    #
    # BRIEF: takes in a list containing the contents of input file and
    # returns a list containing exclusion words
    #
    # PARAMETERS: contents of input file (as a list)
    #
    # RETURN: a list containing exclusion words
    #
    def __getExclusionWords(allFile):
        exclusionWords = ''

        for i in range(2, len(allFile)):
            quotes = re.search(allFile[i], "\"\"\"\"\n")
            if quotes:
                exclusionWords = exclusionWords[:-1]
                break
            else:
                exclusionWords += allFile[i]
                exclusionWords = exclusionWords.replace('\n', ' ')

        return exclusionWords

    #
    # BRIEF: takes in a list containing contents of input file and
    # returns a list of sentences in the file.
    #
    # PARAMETERS: contents of input file (as a list)
    #
    # RETURN: list of sentences in file
    #
    def __getSentences(allFile):
        sentences = []

        index = concord.__getQuotesIndex(allFile) + 1

        # for line in txtFile:
        for i in range(index, len(allFile)):
            if allFile[i] != "\n":
                sentences.append(allFile[i].strip())

        return sentences

    #
    # BRIEF: takes in a list of exclusion words and sentences in input
    # file and returns a list of indexed words/words to capitilize.
    #
    # PARAMETERS: exclusion words and sentences as lists
    #
    # RETURN: list of indexed/capitilized words
    #
    def __getIndexedWords(exclusions, sentences):
        words = []
        indexedWords = []

        for sentence in sentences:
            temp = sentence.split(' ')
            words.append(temp)

        for sentence in words:
            for word in sentence:
                tempStr = r"\b" + word + r"\b"
                found = re.search(tempStr, exclusions, re.IGNORECASE)
                if not found:
                    indexedWords.append(word)

        return indexedWords

    #
    # BRIEF: takes in a list containing words in a sentence
    # and an indexed word and returns the index of the word in the sentence.
    #
    # PARAMETERS: list of words in a sentence and a indexed word
    #
    # RETURN: integer value holding the index of that word in the list
    #
    def __getCapWordIndex(sentence, indexedWord):

        index = 0
        for i in range(len(sentence)):
            if sentence[i].lower() == indexedWord.lower():
                index = i
                break
        return index
    #
    # BRIEF: takes in a list of words in a sentence, the space on the left (20), and
    # the index of the word to capitilize and returns the left substring of desired
    # output.
    #
    # PARAMETERS: list of words in a sentence, integer value of the space on the left
    # of indexed word, and the index of the indexed word.
    #
    # RETURN: left substring of desired output
    #

    def __leftOutput(sentence, leftSpace, capWordIndex):
        leftString = ''
        capWordIndex -= 1

        if capWordIndex < 0:
            return leftString
        else:
            for i in range(capWordIndex, -1, -1):
                if (len(sentence[i]) + 1) > leftSpace:
                    break
                else:
                    leftString = sentence[i] + ' ' + leftString
                    leftSpace -= (len(sentence[i]) + 1)

        return leftString
    #
    # BRIEF: takes in a list of words in a sentence, the space on the right (30 - length of
    # indexed word), and the index of the word to capitilize and returns the right substring of
    # desired output
    #
    # PARAMETERS: list of words in a sentence, integer value of the space on the right of the
    # indexed word, and the index of the indexed word.
    #
    # RETURN: right substring of desired output
    #

    def __rightOutput(sentence, rightSpace, capWordIndex):
        rightString = ''
        capWordIndex += 1

        if capWordIndex >= len(sentence):
            return rightString
        else:
            for i in range(capWordIndex, len(sentence)):
                if len(sentence[i]) > rightSpace:
                    break
                rightString += ' ' + sentence[i]
                rightSpace -= (len(sentence[i]) + 1)

        return rightString

    #
    # BRIEF: takes in a sentence in a list of words in a sentence and a index word
    # and returns a boolean. The boolean is true if the word is found in the sentence,
    # false if otherwise.
    #
    # PARAMETERS: list of words in a sentence and an index word
    #
    # RETURN: boolean (true if word is found, false otherwise)
    #
    def __inSentence(sentence, indexedWord):
        found = False
        for word in sentence:
            if word.lower() == indexedWord.lower():
                found = True
        return found

    #
    # BRIEF: takes in a list of indexed words and a list of sentences in input file
    # and returns a list containing output as detailed in assignment description.
    #
    # PARAMETRS: list of indexed words and list of sentences in input file
    #
    # RETURN: list of desired output
    #
    def __getConcordanceLines(indexedWords, sentences):
        concLines = []

        for word in indexedWords:
            for sentence in sentences:
                tempSentence = sentence.split(' ')
                found = concord.__inSentence(tempSentence, word)

                if found:
                    tempSentence = sentence.split(' ')
                    output = " " * 9

                    index = concord.__getCapWordIndex(tempSentence, word)

                    spaceLeft = 20
                    spaceRight = 30 - len(word)

                    left = concord.__leftOutput(tempSentence, spaceLeft, index)
                    right = concord.__rightOutput(
                        tempSentence, spaceRight, index)

                    indexedWord = word.upper()

                    padding = 20 - len(left)
                    leftPadding = ' ' * padding

                    output = output + leftPadding + left + indexedWord + right

                    if output not in concLines:
                        concLines.append(output)

        return concLines
