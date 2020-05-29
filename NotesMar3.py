class Node():
    def __init__(self, data, nextNode = "None"):
        self.data = data
        self.nextNode = nextNode

class circularSLL():
    def __init__(self):
        self.head = "None"
        self.tail = "None"
        self.size = 0

    def add_head(self, e):
        newNode = Node(e)
        if self.size == 0 and self.head == "None":
            self.head = newNode
            self.tail = newNode
            self.tail.nextNode = self.head
        else:
            newNode.nextNode = self.head
            self.head = newNode
            self.tail.nextNode = self.head

        self.size += 1

#Don't actually need head since the tail is always pointing to the head

    def printReverse(self):
        current = self.tail.nextNode
        circularSLLString = ""
        if self.size == 0:
            print("There are no nodes in the list")
        else:
            while current.nextNode != self.tail.nextNode:
                circularSLLString += str(current.data) + ""
#Create a stack to help print in reverse
