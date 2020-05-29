
#Sari Stissi
#Assignment 4

#while choice is not equal to 6

class Node():
    def __init__(self, data, nextNode = "None"):
        self.data = data
        self.nextNode = nextNode
        
    
class SinglyLinkedList():
    def __init__(self):
        self.head = "None"
        self.tail = "None"
        self.size = 0

    def add_head(self, e):
        newNode = Node(e)
        if self.size == 0 and self.head == "None":
            self.head = newNode
            self.tail = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        
        self.size += 1

    def add_tail(self, e):
        newNode = Node(e)
        if self.size == 0 and self.tail == "None":
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode

        self.size += 1

    def add_before(self, node, e):
        newNode = Node(e)
        currentNode = self.head
        prevNode = "None"
        if self.size == 0:
            print("Error: please add a head or a tail first")
        while currentNode.data != node:
            prevNode = currentNode
            currentNode = currentNode.nextNode
            if currentNode.nextNode == "None":
                print("Error: node not found")
                break
        if prevNode == "None":
            self.add_head(e)
        else:
            newNode.nextNode = currentNode
            prevNode.nextNode = newNode

        self.size += 1

    def remove(self, node):
        currentNode = self.head
        prevNode = "None"
        if self.size == 0:
            print("Error: There are no nodes to remove")
        else:
            while currentNode.data != node:
                prevNode = currentNode
                currentNode = currentNode.nextNode
                if currentNode.nextNode == "None":
                    print("Error: node you're looking for not found")
                    break
            if prevNode == "None":
                if currentNode.nextNode == "None":
                    self.head = "None"
                    self.tail = "None"
                else:
                    self.head = currentNode.nextNode
                    currentNode.nextNode = "None"
            elif currentNode.nextNode == "None":
                prevNode.nextNode = "None"
                self.tail = prevNode
            else:
                prevNode.nextNode = currentNode.nextNode
                currentNode.nextNode = "None"
            self.size -= 1

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
