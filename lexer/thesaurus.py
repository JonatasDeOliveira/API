# encoding: utf-8
import json

def _removeDuplicates(query):
    result = []
    for q in query:
       if q not in result:
           result.append(q)
    return result

def _load(word):
    c = word[0]
    path = "lexer/thesaurus/thesaurus_update/" + c + ".json"
    with open(path, 'r') as fileIn:
        syn = json.load(fileIn)
        fileIn.close()
    return syn

def synonyms(word):
    ls = []
    
    syn = _load(word)
    dWord = syn.get(word)
    if dWord is not None:
        ctxKeys = dWord.keys()
        relev = 3
        while relev > 0:
            for key in ctxKeys:
                dCtx = dWord.get(key)
                if isinstance(dCtx,dict):
                    dSyn = dCtx.get("synonyms")
                    if dSyn.has_key(str(relev)):
                        ls.extend(dSyn.get(str(relev)))
                else:
                    ls.extend(synonyms(dCtx.encode("utf-8")))
                    relev = 0
            relev -= 1
    
    return _removeDuplicates(ls)


def antonyms(word):
    la = []
    
    syn = _load(word)
    dWord = syn.get(word)
    if dWord is not None:
        ctxKeys = dWord.keys()
        relev = 3
        while relev > 0:
            for key in ctxKeys:
                dCtx = dWord.get(key)
                if isinstance(dCtx,dict):
                    dSyn = dCtx.get("antonyms")
                    if dSyn.has_key(str(relev)):
                        la.extend(dSyn.get(str(relev)))
                else:
                    la.extend(antonyms(dCtx.encode("utf-8")))
                    relev = 0
            relev -= 1
    
    return _removeDuplicates(la)
    
