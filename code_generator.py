import random, string, time

codeTemplate = 'XXXX-XXXX-XXXX'
noOfCodes = 100
chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
excludedChars = 'oO0'
fileName = 'codes'
fileFormat = 'txt'

listOfCodes = []

def excludeChars():

    global chars, excludedChars
    excludedDict = dict.fromkeys([ord(c) for c in excludedChars], None)
    chars = chars.translate(excludedDict)

def generateCode(template, useChars):

    newCode = ''
    for chr in template:
        if chr == 'X':
            newCode += random.SystemRandom().choice(useChars) 
        else:
            newCode += chr
    
    return newCode

def generateAllCodes():

    global noOfCodes, listOfCodes
    while len(listOfCodes) < noOfCodes:
        
        addCode = generateCode(codeTemplate, chars) + '\n'
        if addCode not in listOfCodes:
            listOfCodes.append(addCode)

def toTxtFile(name):

    with open('{0}_{1}.{2}'.format(name, time.strftime("%Y-%m-%d-%H_%M_%S"),fileFormat), "w") as f:
        f.writelines(listOfCodes)
#-----------------------------------------------------------

excludeChars()
generateAllCodes()
toTxtFile(fileName)

print ('Used chars: {0}'.format(chars))
print ('Timestamp: {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
print ('List of codes:\n{0}'.format(listOfCodes))
