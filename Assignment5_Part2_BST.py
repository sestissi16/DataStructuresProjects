#Assignment 5 Part 2
#Sari Stissi

from Assign5Part1BST256Stissi import *

def findSmallestNode(bst, node):
    #need to go right once and as left as possible
    #if there is no right branch we need to go up once (to the right)
    #in the case of the lestmost leaf there would be nothing to return
    currentNode = bst.findNode(node)
    smallestBiggerNode = None
    if currentNode.right != None:
        smallestBiggerNode = currentNode.right
        currentNode = currentNode.right
        while currentNode.left != None:
            smallestBiggerNode = currentNode.left
            currentNode = currentNode.left
    elif currentNode.parent.data > currentNode.data:
        smallestBiggerNode = currentNode.parent
    else:
        return("The node is the largest node in the tree")
    return smallestBiggerNode.data

def findLargestNode(bst, node):
    currentNode = bst.findNode(node)
    largestSmallerNode = None
    if currentNode.left != None:
        largestSmallerNode = currentNode.left
        currentNode = currentNode.left
        while currentNode.right != None:
            largestSmallerNode = currentNode.right
            currentNode = currentNode.right
    elif currentNode.parent.data < currentNode.data:
        largestSmallerNode = currentNode.parent
    else:
        return("The node is the smallest node in the tree")
    return largestSmallerNode.data

def inOrderTraversal(tree):
    currentNode = tree.root
    arrayToKeepTrack = []
    actualElements = []
    finished = False

    while finished == False:
        if currentNode != None:
            arrayToKeepTrack.append(currentNode)
            currentNode = currentNode.left
        else:
            if len(arrayToKeepTrack) > 0:
                currentNode = arrayToKeepTrack.pop()
                actualElements.append(currentNode.data)
                currentNode = currentNode.right
            else:
                finished = True
    return actualElements
                
    

#I'm assume that identical set of elements means that they have exactly
#the same element but they don't have to be in the same places in the tree
def checkElements(bst1, bst2):
    #I'm defining an inorder traversal function for convience
    elementsInFirst = inOrderTraversal(bst1)
    elementsInSecond = inOrderTraversal(bst2)
    #Inorder traversal should create a sorted array so we can just compare them directly
    if elementsInFirst == elementsInSecond:
        return True
    else:
        return False
    

    
"""if __name__ == "__main__":
    b = BST()
    b.add_node(20)
    b.add_node(17)
    b.add_node(17)
    b.add_node(25)
    b.add_node(22)
    b.add_node(18)
    b.add_node(5)
    b.add_node(35)
    b.add_node(24)
    b.add_node(40)
    b.add_node(23)
    b.add_node(24)
    c = BST()
    c.add_node(25)
    c.add_node(20)
    c.add_node(5)
    c.add_node(17)
    c.add_node(35)
    c.add_node(40)
    c.add_node(18)
    c.add_node(17)
    c.add_node(22)
    c.add_node(23)
    c.add_node(24)
    c.add_node(24)
    print(checkElements(b, c))"""
    
