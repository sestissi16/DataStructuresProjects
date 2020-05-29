
#Sari Stissi
#Assignment 4

#while choice is not equal to 6

#create a class for the Node element
class Node():
    #initialize the node
    def __init__(self, data, nextNode = "None"):
        self.data = data
        self.nextNode = nextNode
        
#class for the singly linked list
class SinglyLinkedList():
    #initialize the list
    def __init__(self):
        self.head = "None"
        self.tail = "None"
        self.size = 0

    #function to add a head to the list
    def add_head(self, e):
        newNode = Node(e)

        #if there isn't anything in the list and there is no head node
        if self.size == 0 and self.head == "None":
            #add this new node as the head and the tail
            self.head = newNode
            self.tail = newNode

        #if there are nodes in the list and there is a head node
        else:
            #link the old head node to the new node
            newNode.nextNode = self.head
            self.head = newNode
        
        #update the size of the list
        self.size += 1

    #function to add a tail to the list
    def add_tail(self, e):
        newNode = Node(e)

        #if list is empty
        if self.size == 0 and self.tail == "None":
            #make the new node buth the head and the tail
            self.head = newNode
            self.tail = newNode

        #if there are elements in the list
        else:
            #make the old tail link to the new node and make the new node the actual tail
            self.tail.nextNode = newNode
            self.tail = newNode

        #update the size of the list
        self.size += 1

    #function to add a new element before a certain element in the list
    def add_before(self, node, e):
        #get the new node to add
        newNode = Node(e)

        #get the head from the list
        currentNode = self.head
        #save the last element you were looking at
        prevNode = "None"

        #if there are no elements it prints an error
        if self.size == 0:
            print("Error: please add a head or a tail first")

        else:
            #while the current node doesn't equal the node we're looking for
            while currentNode.data != node:
                #update prevNode and currentNode
                prevNode = currentNode
                currentNode = currentNode.nextNode

                #if it gets to the the end of the list then the node to place before was not found
                if currentNode.nextNode == "None":
                    print("Error: node not found")
                    break
            #if the node to add the new one before is the first in the list
            if prevNode == "None":
                #add the new node as the head
                self.add_head(e)
            else:
                #add the new node before the element
                newNode.nextNode = currentNode
                prevNode.nextNode = newNode

        #update the size of the list
        self.size += 1

    #function to remove an element from the list
    def remove(self, node):
        #get the first element in the list
        currentNode = self.head
        #var to keep track of the previous node checked
        prevNode = "None"

        #check if the list is empty
        if self.size == 0:
            print("Error: There are no nodes to remove")
        else:

            #search for the element to remove
            while currentNode.data != node:
                prevNode = currentNode
                currentNode = currentNode.nextNode
                if currentNode.nextNode == "None":
                    print("Error: node you're looking for not found")
                    break
            
            #if the element is at the beginning of the list
            if prevNode == "None":
                #if the element is also the only element in the list
                if currentNode.nextNode == "None":
                    self.head = "None"
                    self.tail = "None"
                else:
                    self.head = currentNode.nextNode
                    currentNode.nextNode = "None"

            #if the element is at the end of the list
            elif currentNode.nextNode == "None":
                prevNode.nextNode = "None"
                self.tail = prevNode
            else:
                prevNode.nextNode = currentNode.nextNode
                currentNode.nextNode = "None"

            #update the size of the list
            self.size -= 1

    #function to print the current list
    def printList(self):
        current = self.head
        linkedListString = ""
        if self.size == 0:
            print("There are no nodes in the list")
        else:
            while current.nextNode != "None":
                linkedListString += str(current.data) + ", "
                current = current.nextNode
            linkedListString += str(self.tail.data)
            print(linkedListString)
        
        
if __name__ == "__main__":
    s = SinglyLinkedList()
    print("Please select one of the following choices: ")
    print("1. add at the head of the list")
    print("2. add at the tail of the list")
    print("3. add before the node with data")
    print("4. remove node with data")
    print("5. print the list")
    print("6. quit")
    userInput = input("Type in a number: ")
    print("-------------------------------------")
    print()
    
    while userInput == '' or int(userInput) < 6:
        if userInput == '':
            print("Please enter a valid number")
        elif int(userInput) == 1:
            headInfo = input("Please enter the key for the new node: ")
            s.add_head(headInfo)
        elif int(userInput) == 2:
            tailInfo = input("Please enter the key for the new node: ")
            s.add_tail(tailInfo)
        elif int(userInput) == 3:
            userNodeKey = input("Please enter the node key you want to add something before: ")
            userNewKey = input("Please enter the new node key: ")
            s.add_before(userNodeKey, userNewKey)
        elif int(userInput) == 4:
            userRemNode = input("Please enter the node key which you want to remove: ")
            s.remove(userRemNode)
        elif int(userInput) == 5:
            s.printList()
        print()
        print("---------------------------------------")
        print("Please select one of the following choices: ")
        print("1. add at the head of the list")
        print("2. add at the tail of the list")
        print("3. add before the node with data")
        print("4. remove node with data")
        print("5. print the list")
        print("6. quit")
        userInput = input("Type in a number: ")
        print("---------------------------------------")
        print()
    if int(userInput) > 6:
        print("Please enter a valid choice number.")
    else:
        print("Thank you for using this program")
