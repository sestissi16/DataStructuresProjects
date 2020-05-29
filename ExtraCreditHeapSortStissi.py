#Sari Stissi
#Extra Credit Assignment
#heapSort(A)

def makeHeap(A, n, i):
    rootNode = i
    leftNode = (2 * i) + 1
    rightNode = (2 * i) + 2

    if leftNode < n and A[i] < A[leftNode]:
        rootNode = leftNode

    if rightNode < n and A[rootNode] < A[rightNode]:
        rootNode = rightNode

    if rootNode != i:
        A[i], A[rootNode] = A[rootNode], A[i]

        makeHeap(A, n, rootNode)

def heapSort(A):
    n = len(A)

    for i in range(n, -1, -1):
        makeHeap(A, n, i)

    for i in range((n-1), 0, -1):
        A[i], A[0] = A[0], A[i]
        makeHeap(A, i, 0)

if __name__ == "__main__":

    A = [89, 2, 12, 13, 5, 6, 7]
    oldA = A
    heapSort(A)
    n = len(A)
    print("Here is an example of a an array sorted by Heap Sort: ")
    print("At first it was: " + str(oldA) + " and then it became: " + str(A))
    
