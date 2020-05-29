#Assignment 5
#Sari Stissi
#used this website to help me with the height method because I was severely struggling with how to make sure it found the longest path
#https://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/

class Node():
    def __init__(self, data):

        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        
class BST():
    def __init__(self, node = None):

        self.root = node
        
    def findNode(self, node):
        currentNode = self.root
        nodeFound = None
        while nodeFound == None:
            if node == currentNode.data:
                nodeFound = currentNode
            elif node < currentNode.data:
                currentNode = currentNode.left
            elif node > currentNode.data:
                currentNode = currentNode.right
        return nodeFound

    def add_node(self, data):
        newNode = Node(data)
        #var to keep track of where we're at
        currentNode = self.root
        #my code allows duplicates to be added as a leaf in the tree
        if self.root == None:
            self.root = newNode
        else:
            while newNode.data < currentNode.data or newNode.data >= currentNode.data:
                if newNode.data < currentNode.data:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        newNode.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.left
                elif newNode.data >= currentNode.data:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        newNode.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.right
                else:
                    print("Node cannot be added")
    def height(self, node):
        arrayOfItems = []
        currentNode = self.findNode(node)
        arrayOfItems.append(currentNode)
        height = 0
        while True:
            nodeCount = len(arrayOfItems)
            if nodeCount == 0:
                return height -1
            height += 1
            while nodeCount > 0:
                checkNode = arrayOfItems[0]
                arrayOfItems.pop(0)
                if checkNode.left != None:
                    arrayOfItems.append(checkNode.left)
                if checkNode.right != None:
                    arrayOfItems.append(checkNode.right)
                nodeCount -= 1

    def depth(self, node):
        nodeFound = False
        currentNode = self.root
        depth = 0
        while nodeFound == False:
            if node == currentNode.data:
                nodeFound = True
                return depth
            elif node > currentNode.data:
                currentNode = currentNode.right
                depth += 1
            elif node < currentNode.data:
                currentNode = currentNode.left
                depth += 1
                
    def printTree(self, root = 0):
        #I could not figure out how to do printTree well without recursion
        if self.root == None:
            return "There are no elements in this tree to print"
        else:
            if root == 0:
                root = self.root
            if root != None:
                self.printTree(root.left)
                self.printTree(root.right)
                print(root.data)
        
            
            
                    
"""if __name__ == "__main__":
    b = BST()
    b.add_node(20)
    b.add_node(17)
    b.add_node(25)
    b.add_node(22)
    b.add_node(18)
    b.add_node(5)
    b.add_node(35)
    b.add_node(24)
    b.add_node(40)
    b.add_node(23)
    node = b.root.data
    print(b.height(node))
    b.printTree()"""
