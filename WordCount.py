#Sari Stissi
#Assignment 6

from SeparateChainingMap import SeparateChainingMap

def WordCount(filename):
    fname = open(filename, 'r')
    SCM = SeparateChainingMap()
    for words in fname.read().split():
        if SCM.contains(word):
            SCM.HashMapBase.setitem(word, SMC[word] += 1)
        else:
            SCM.HashMapBase.setitem(word, 1)
        return SCM.iter()
    
