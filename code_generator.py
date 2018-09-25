#Program vygeneruje n kodov v zadanom formate, pricom kody sa neopakuju a skladaju sa len zo zadefinovanych znakov. Nasledne ich exportne do .txt suboru.
#pozn.: program sa zacykli ak ma vygenerovat viac kodov ako je moznych jedninecnych kombinacii so zadanymi znakmi

import random, string, time

codeTemplate = 'XXXX-XXXX-XXXX' #sablona pre kody (X-ka sa nahradia nahodnym znakom)
noOfCodes = 100 #pocet vygenerovanych kodov
listOfCodes = []
chars = string.ascii_uppercase + string.digits #+ string.ascii_lowercase #string vsetkych znakov, z ktorych sa moze generovat kod
excludedChars = 'oO0' #string znakov, ktore sa nepouziju pri generovani (napr. pre vylucenie O a 0)
fileName = 'kody' #nazov txt suboru na export kodov
fileFormat = 'txt'

#z chars vyhodi vsetky excludedChars (viac v poznamkach na konci)
def excludeChars():

    global chars, excludedChars
    excludedDict = dict.fromkeys([ord(c) for c in excludedChars], None)
    chars = chars.translate(excludedDict)

def generateCode(template, useChars):

    newCode = ''
    for chr in template:
        if chr == 'X':
            #choice() vyberie nahodny prvok zo stringu. Funguje aj bez SystemRandom() ale s tym je to vraj viac secure
            newCode += random.SystemRandom().choice(useChars) 
        else:
            newCode += chr
    
    return newCode

def generateAllCodes():

    global noOfCodes, listOfCodes
    while len(listOfCodes) < noOfCodes:
        
        addCode = generateCode(codeTemplate, chars) + '\n'
        #za kazdy kod sa prida novy riadok (\n) kvoli formatovaniu v .txt
        if addCode not in listOfCodes:
            listOfCodes.append(addCode)

            
#vytvori txt file podla zadaneho mena a aktualneho timestampu a vlozi don vygenerovane kody
def toTxtFile(name):

    with open('{0}_{1}.{2}'.format(name, time.strftime("%Y-%m-%d-%H_%M_%S"),fileFormat), "w") as f:
        f.writelines(listOfCodes)
#-----------------------------------------------------------

excludeChars()
generateAllCodes()
toTxtFile(fileName)

print ('Pouzite znaky: {0}'.format(chars))
print ('Timestamp: {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
print ('Zoznam kodov:\n{0}'.format(listOfCodes))

#-----------------------------------------------------------
'''
excludeChars()
    pozn.: dalo by sa pouzit aj string = string.replace("stary_znak","novy_znak") - v pythone su stringy immutable (nemozu sa menit) a preto tento sposob vytvara novu kopiu daneho stringu (pozn.: pri tomto programe by to bolo uplne jedno ale je good practice a programovo efektivnejsie robit to sposobom ktory je tu pouzity) (zdroj: https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python)
    
    Metoda translate zmeni znaky v stringu podla dictionary, ktory je jej jedinym a povinnym atributom (napr.: dict = {ord(A): ord(B)} bude hovorit ze kazde 'A' sa ma zmenit na 'B', zaroven ale translate nepracuje s charmi samotnymi ale s ich ASCII hodnotami - preto ten ord()).

    [ord(c) for c in excludedChars] - tato cast kodu vytvori zo stringu excludedChars pole, ktoreho prvkami su jednotlive znaky z excludedChars.
    Toto pole je nasledne prvym parametrom metody dict.fromkeys, ktora robi z pola dictionary. Druhym parametrom metody su hodnoty pre jednolive kluce, v tomto pripade None. Vytvoreny dictionary teda vyzera napr. takto: excludedDict = {72 : None, 43 : None, 77 : None}
    Tento dictionary nakoniec ide to metody translate, ktora na zaklade neho zmeni string chars - vsetky znaky zo slovnika nahrani None - tzn. nicmi = vyhodi ich
    
'''

