letterFreq = []
def getfreq(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.upper()
    charFreq = []
    textLen = len(text)
    freq = 0
    incl = False
    for x in range(0,textLen):
        char = ord(text[x])
        freq = 0
        for item in charFreq:
            incl = item[0] == chr(char)
            if(incl):
                item[1] = float(item[1]) + float(1/(textLen))
                break
        if(not incl):
            charFreq.append([chr(char), float(1/textLen)])
    return(charFreq)

def calcdiff(table1, table2):
    diff = 0
    for i in range(0,25):
        diff += abs(float(table1[i][1]) - float(table2[i][1]))
    return diff

with open('letter_freq.txt', 'r') as letter_freq:
    for line in letter_freq:
        splitLine = line.strip().split('\t')
        letterFreq.append(splitLine)
    #print(letterFreq)

with open('secret_files/secret0.txt', 'r') as secret:
    textFreq = getfreq(str(secret.read()))
    print(textFreq)
    print(calcdiff(letterFreq, textFreq))