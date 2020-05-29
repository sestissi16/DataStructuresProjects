#Sari Stissi
#Assignment 3

from Assignment3_stackClass import *

def isPair(character1, character2):
    if character1 == "(" and character2 == ")":
        return True
    elif character1 == "{" and character2 == "}":
        return True
    elif character1 == "[" and character2 =="]":
        return True
    else:
        return False
    
def isBalanced(string):
    characterStack = Stack()
    print(characterStack.stackArray)
    for item in string:
        print(item)
        if (item == '(' or item == '{' or item == '['):
            characterStack.push(item)
        if (item == ')' or item == '}' or item == ']'):
            if characterStack.isEmpty():
                return False
            elif not isPair(characterStack.pop(), item):
                return False
        print(characterStack.stackArray)
    print(characterStack.stackArray)
    if characterStack.isEmpty():
        return True
    else:
        return False
    
