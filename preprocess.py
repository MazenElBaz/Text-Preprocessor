# ----------------------------
# Name: Mazen ElBaz
# Date: Oct. 2018
# Exercise 4: Text Preprocessor
# ----------------------------


import sys


def checkMode():

    """
    Checks to see if the user entered an optional command line
    argument(mode)

    Argument:
    None

    Returns:
    True: if the user entered a mode
    False: if there is no mode to analyze
    """
    # try and except is used to avoid an index out of range error when the
    # user doesn't include a mode
    try:

        if sys.argv[1]:
            return True

    except IndexError:

        return False


def analyzeCommandLine(flag0):

    """
    Analyzes the mode typed by the user, and error handles invalid mode

    Argument:
    flag0: a boolean variable that is True if the user typed a mode, and
    False otherwise

    Returns:
    True/False, True/False, True/False: 3 boolean variables that will
    determine which functions will be executed(which processing steps will
    be completed)
    """

    if flag0:

        if sys.argv[1] == 'keep-digits':
            # since the mode is keep-digits, a False will be passed on to
            # the function checkNumbers() to stop it from removing numbers
            # from words
            return(True, False, True)
        elif sys.argv[1] == 'keep-stops':
            return(True, True, False)
        elif sys.argv[1] == 'keep-symbols':
            return(False, True, True)
        else:
            print('Invalid mode \nThere are only 3 valid modes: \n' +
                  '1) "keep-digits" \n2) "keep-stops" \n3) ' +
                  '"keep-symbols" \nIt should be in the following' +
                  ' format: "python3 preprocess.py <mode>" \nIf you wish' +
                  ' to run the program without the modes above, you can' +
                  ' just type: "python3 preprocess.py"')

            sys.exit(1)
    # if flag0 is False(ie the user didn't type a mode) pass True to all
    # 3 functions so that all processing steps are executed
    else:

        return(True, True, True)


def lowerWords(wordsListV0):

    """
    converts all words in a list to lowercase

    Argument:
    wordsListV0: a list of the tokens entered by the user

    Returns:
    wordsListV1: the new version of the list of words with all the words
    converted to lowercase
    """

    wordsListV1 = []

    for word in wordsListV0:

        wordsListV1.append(word.lower())

    return wordsListV1


def removeNonAlNum(wordsListV1, flag1):

    """
    removes all punctuation and symbols from the list of words

    Argument:
    wordsListV1: a list of words with all the words in lowercase
    flag1: if True, the function will remove all punctuation and symbols and
    if False, the function will not change the list of words

    Returns:
    wordsListV2: the new version of the list of words with all the
    punctuation and symbols removed from words
    wordsListV1: the list passed to the function will be returned as it is
    if flag1 is False
    """

    wordsListV2 = []

    if flag1:

        for word in wordsListV1:

            for character in word:

                if not character.isalnum():
                    # if a non-alphanumeric character is found, remove it
                    # from the word and replace it with empty string
                    word = word.replace(character, '')

            wordsListV2.append(word)

        return wordsListV2

    else:

        return wordsListV1


def checkNumbers(wordsListV2, flag2):

    """
    removes all numbers unless the token consists only of numbers

    Argument:
    wordsListV2: a list of words with all the words in lowercase and
    punctuation and symbols removed
    flag2: if True, the function will remove all numbers from non-numeric
    tokens and if False, the function will not change the list of words

    Returns:
    wordsListV3: the new version of the list of words with all the numbers
    removed from non-numeric tokens
    wordsListV2: the list passed to the function will be returned as it is
    if flag2 is False
    """

    wordsListV3 = []

    if flag2:

        for word in wordsListV2:
            # if the token doesn't consist only of numbers, check every
            # character of that token and remove any number character
            if not word.isnumeric():
                for character in word:
                    if character.isnumeric():
                        word = word.replace(character, '')

            wordsListV3.append(word)

        return wordsListV3

    else:

        return wordsListV2


def removeStopWords(wordsListV3, flag3):

    """
    removes all stopwords from the list

    Argument:
    wordsListV3: a list of words with all the words in lowercase,
    punctuation and symbols removed, and numbers removed from non-numeric
    tokens
    flag3: if True, the function will remove stopwords and if False, the
    function will not change the list of words

    Returns:
    processedWords: the new version of the list of words with all the
    stopwords removed from the list
    wordsListV3: the list passed to the function will be returned as it is
    if flag3 is False
    """

    processedWords = []
    stopWords = ("i me my myself we our ours ourselves you your yours" +
                 " yourself yourselves he him his himself she her hers" +
                 " herself it its itself they them their theirs" +
                 " themselves what which who whom this that these those" +
                 " am is are was were be been being have has had having" +
                 " do does did doing a an the and but if or because as" +
                 " until while of at by for with about against between" +
                 " into through during before after above below to from" +
                 " up down in out on off over under again further then" +
                 " once here there when where why how all any both each" +
                 " few more most other some such no nor not only own" +
                 " same so than too very s t can will just don" +
                 " should now").split()

    if flag3:

        for word in wordsListV3:
            # only add the words that are not stopwords to the new list
            # processedWords
            if word not in stopWords:
                processedWords.append(word)

        return processedWords

    else:

        return wordsListV3


def main():

    flag0 = checkMode()
    flag1, flag2, flag3 = analyzeCommandLine(flag0)
    lineWords = input().split()
    process1 = lowerWords(lineWords)
    process2 = removeNonAlNum(process1, flag1)
    process3 = checkNumbers(process2, flag2)
    process4 = removeStopWords(process3, flag3)
    # converts the final version of the list of words to a space-separated
    # string and stores it in the variable finalProcess
    finalProcess = ' '.join(process4)
    print(finalProcess)


if __name__ == "__main__":

    main()
