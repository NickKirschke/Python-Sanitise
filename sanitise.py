'''
November 9, 2015

@author: Nick Kirschke
'''
import re
from string import maketrans

def blackout(email, words):
    lowerEmail = email.lower()
    lowerWords = []
    ''' make all the words lower case '''
    for s in words:
        zz = s.lower()
        lowerWords.append(zz)
    ''' remove unwanted characters from the lower case email then split, translate replaces all
    of these specific characters with spaces'''
    inTable = '-(),*#$%^&_'
    outTable = '           '
    table = maketrans(inTable, outTable)
    cleanEmail = lowerEmail.translate(table)
    ''' Split based on the specific punctuation '''
    splitEmail = re.split("[.?!]+", cleanEmail )
    ''' Use search method and if it returns none then boolean equals false, increment 
        stringCount and continue'''
    stringBool = []
    for string in splitEmail:
        boolVal = False
        for wrd in lowerWords:
            ''' Make the format of the word require no other letters 
            around it so it can't be detected inside other words'''
            t = re.compile(r'\b{0}\b'.format(wrd))
            v = t.search(string)
            print(string)
            print (wrd)
            print(v)
            if v is None:
                `````````print("Did not match the word, check next one")
            else:
                boolVal = True
                stringBool.append(boolVal)
                print("Matching word was found move to next string")
                break
        if boolVal is False:
            stringBool.append(boolVal)
    ''' I now have a list of which strings have bad words in them so
        now I need to just put @ symbols in all the spots of those strings '''
    print(stringBool)
    splitAnswer = list(email)
    ''' Go character by character, checking for .!? and when encountering one
        increment counter and check boolean array to see if there was a bad word '''
    boolCount = 0
    m = 0
    while m < len(splitAnswer):
        if splitAnswer[m] == '?' or splitAnswer[m] == '.' or splitAnswer[m] == '!':
            if stringBool[boolCount] == True:
                splitAnswer[m] = '@'
                boolCount += 1
            else:
                boolCount += 1
        else: 
            if stringBool[boolCount] == True:
                splitAnswer[m] = '@'
        m += 1
    finalAnswer = "".join(splitAnswer)
    return finalAnswer