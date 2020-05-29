#Sari Stissi
#Assingment 4

from Assign4SinglyLinkedList256Stissi import *
from circqueueClassAssignment3Stissi import *
import time

class LinkedQueue():
    def __init__(self):
        self.queueList = SinglyLinkedList()
        self.front = self.queueList.head
        self.rear = self.queueList.tail
        self.size = self.queueList.size

    def isEmpty(self):
        return self.front == "None" and self.rear == "None"

    def enqueue(self, e):
        newNode = Node(e)
        if self.size == 0:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.nextNode = newNode
            self.rear = newNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("There are no nodes to remove in the list")
        else:
            oldHead = self.front
            if oldHead.nextNode == "None":
                self.front = "None"
                self.rear = "None"
            else:
                self.front = oldHead.nextNode
            self.size -= 1
            return oldHead.data
            

    def printQueue(self):
        current = self.front
        linkedListString = ""
        if self.size == 0:
            print("There are no nodes in the list")
        else:
            while current.nextNode != "None":
                linkedListString += str(current.data) + ", "
                current = current.nextNode
            linkedListString += str(self.rear.data)
            print(linkedListString) 

if __name__ == "__main__":
    startTimeOfEntireProcess = time.clock()
    lq = LinkedQueue()
    cq = Circ_Queue()
    startTimeEnqueueLinked = time.clock()
    for i in range(50000):
        lq.enqueue(i)
    endTimeEnqueueLinked = time.clock()
    
    startTimeEnqueueCirc = time.clock()
    for i in range(50000):
        cq.enqueue(i)
    endTimeEnqueueCirc = time.clock()
    
    startTimeDequeueLinked = time.clock()
    for i in range(25000):
        lq.dequeue()
    endTimeDequeueLinked = time.clock()
    
    startTimeDequeueCirc = time.clock()
    for i in range(25000):
        cq.dequeue()
    endTimeDequeueCirc = time.clock()
    
    startTimeEnqueue2Linked = time.clock()
    for i in range(50000, 100000):
        lq.enqueue(i)
    endTimeEnqueue2Linked = time.clock()
    
    startTimeEnqueue2Circ = time.clock()
    for i in range(50000, 100000):
        cq.enqueue(i)
    endTimeEnqueue2Circ = time.clock()
   
    startTimeRemoveLinked = time.clock()
    for i in range(lq.size):
        lq.dequeue()
    endTimeRemoveLinked = time.clock()
    
    startTimeRemoveCirc = time.clock()
    for i in range(cq.size):
        cq.dequeue()
    endTimeRemoveCirc = time.clock()

    endTimeOfEntireProcess = time.clock()

    print("Time required for enqueue on the LinkedQueue is " + str(endTimeEnqueueLinked - startTimeEnqueueLinked) + " seconds")
    print("Time required for enqueue on the CircularQueue is " + str(endTimeEnqueueCirc - startTimeEnqueueCirc) + " seconds")
    print()
    print("-----------------------------------------------------------------------------")
    print()
    print("The time required for dequeue on the LinkedQueue is " + str(endTimeDequeueLinked - startTimeDequeueLinked) + " seconds")
    print("The time required for dequeue on the CircularQueue is " + str(endTimeDequeueCirc - startTimeDequeueCirc) + " seconds")
    print()
    print("------------------------------------------------------------------------------")
    print()
    print("The time required for the 2nd enqueue on the LinkedQueue is " + str(endTimeEnqueue2Linked - startTimeEnqueue2Linked) + " seconds")
    print("The time required for the 2nd enqueue on the CircularQueue is " + str(endTimeEnqueue2Circ - startTimeEnqueue2Circ) + " seconds")
    print()
    print("------------------------------------------------------------------------------")
    print()
    print("The time required to remove everything from LinkedQueue " + str(endTimeRemoveLinked - startTimeRemoveLinked) + " seconds")
    print("The time required to remove everything from CircularQueue " + str(endTimeRemoveCirc - startTimeRemoveCirc) +  " seconds")
    print()
    print("-------------------------------------------------------------------------------")
    print()
    print("Total time it took to run all of this " + str(endTimeOfEntireProcess - startTimeOfEntireProcess) + " seconds")
    
   
