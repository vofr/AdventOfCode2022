suma=0

def readFile(fileName):
    global suma
    with open(fileName, 'r') as f:
        for l in f:
            convertFromStfu(l)
    print (suma)
    print(fromstfutodec(int(suma)))

def convertFromStfu (number):
    global suma
    nr=""
    inverse=0
    nrFinal=0
    count=len(number)-2
    print(number[inverse])
    for i in range (count, -1, -1):
        inverse=len(number)-2-i
        nr=number[i]
        if(nr == "2"):
            nrFinal += 2 * pow(5,inverse)
        elif (nr == "1"):
            nrFinal += 1 * pow(5, inverse)
        elif (nr == "0"):
            nrFinal += 0 * pow(5, inverse)
        elif (nr == "-"):
            nrFinal += -1 * pow(5, inverse)
        else :
            nrFinal += -2 * pow(5, inverse)
    suma+=nrFinal

def fromstfutodec(number):
    if(number):
        a, b=divmod(number+2,5)
        return fromstfutodec(a) + '=-012'[b]
    else :
        return""



# Press the green button in the gutter to run the script.
if _name_ == '_main_':
    readFile('date.txt')
    #convertFromStfu("21")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
