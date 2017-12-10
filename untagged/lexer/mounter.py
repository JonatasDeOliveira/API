import json
import thesaurus

def load(path):
    path = path+".json"
    with open(path, 'r') as fileIn:
        syn = json.load(fileIn)
        fileIn.close()
    return syn
    
def write(dic, letter):
    with open('thesaurus/synonyms_occurrence_order/'+letter+'.json', 'w') as fileOut:
        json.dump(dic, fileOut)
    
occDict = load("dataset_sortby_occurence")
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"]
#letters = ["z"]

for letter in letters:
    wordsDict = load("thesaurus/thesaurus_update/"+letter)
    newDict = {}
    words = wordsDict.keys()
    for word in words:
        wordDict = wordsDict.get(word)
        ctxs = wordDict.keys()
        newAntDict = {}
        aux = []
        maxnum = 0
        for ctx in ctxs:
            synAntDict = wordDict.get(ctx)
            if isinstance(synAntDict,dict):
                antDict = synAntDict.get("synonyms")
                nums = antDict.keys()
                for num in nums:
                    l = antDict.get(num)
                    for elem in l:
                        occNum = occDict.get(elem)
                        if occNum > maxnum:
                            maxnum = occNum
                        newAntDict[elem] = occNum
            else:
                newAntDict["goto"] = synAntDict
                
        if maxnum != 0:
            auxList = []
            chaves = newAntDict.keys()
            for chave in chaves:
                a = (chave, newAntDict.get(chave))
                auxList.append(a)
            auxList.sort(key=lambda x: x[1], reverse = True)
            newAntDict = {}
            for elem in auxList:
                aux.append(elem[0])
            newDict[word] = aux
        else:
            newDict[word] = newAntDict
    write(newDict, letter)
    

        
