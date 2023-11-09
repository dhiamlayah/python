def resultPrinted (nbsA,operations,nbsB):
    firstNumbers = ''
    secondNumbers = ''
    lignes=''
    for i in range(len(nbsA)):
        maxi=max(len(nbsA[i]),len(nbsB[i]))
        firstNumbers=firstNumbers+"   "+(maxi-len(nbsA[i]))*' '+nbsA[i]
        secondNumbers=secondNumbers+"  "+operations[i]+(maxi-len(nbsB[i]))*' '+nbsB[i]
        lignes=lignes+'  '+(maxi+1)*'-'
    print(firstNumbers)
    print(secondNumbers)
    print(lignes)

def somme (nbsA,operations,nbsB):
    somme =''
    for i in range(len(nbsA)):
        maxi=max(len(nbsA[i]),len(nbsB[i]))
        if(operations[i]=='+'):
            result = int(nbsA[i])+int(nbsB[i])
        if(operations[i]=='-'):
            result = int(nbsA[i])-int(nbsB[i])
        stringResult=str(result)
        somme=somme+'  '+(maxi-len(stringResult)+1)*' '+stringResult
    print(somme)
def arithmetic_arranger (listOfNumbers,showResult=False):
    operations=[]
    numbersA=[]
    numbersB=[]
    for i in listOfNumbers :
        l=i.split()
        numbersA.append(l[0])
        operations.append(l[1])
        numbersB.append(l[2])
    resultPrinted(numbersA,operations,numbersB)
    if(showResult):
        somme(numbersA,operations,numbersB)
   
        
    

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
