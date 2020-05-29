#Sari Stissi
#Assignment 2
#https://docs.python.org/3/library/functions.html ; used website to find ord()
#https://www.tutorialspoint.com/python/string_upper.htm ; used to find .upper()
#https://docs.python.org/3/library/sys.html ; used for maxsize


def isAnagram(A, B):
    """
        Ord returns an integer representing the Unicode code point of that
        character.
        
        Each string could be represented as a sum of these numbers.
        
        If both strings are an anagram then both strings have the same letters
        and therefore have the same sum of integers representing the Unicode
        code point.
        
        == returns true or false so I can use that to see if they're anagrams
    """
    if A or B == "":
        raise ValueError("Cannot pass an empty string")
    if A or B == None:
        raise ValueError("Cannot pass an empty string")
    numA = 0
    numB = 0
    for letter in A:
        numA += ord(letter.upper())
    for letter in B:
        numB += ord(letter.upper())

    return numA==numB


def findNearest(A, key): 
    firstTime = True
    #keep track of the difference between key and element
    #the smaller the difference the closer to the number
    closestDif = 0
    #keep track of what has been the closest element so far
    #ideally there won't be a 0 in the list
    closestElm = 0
    #goes through all the elements in the list
    for element in A:
        #firstTime sets the initial closestDif and closestElm
        #so that the program as something to check the other elements with
        if firstTime:
            #makes firstTime False so that it will go on to do what
            #I want it to do for the other elements
            firstTime = False
            #this is me making sure all results are positive
            #so that I can compare them more accurately
            if key > element:
                #makes difference between key and element
                #the new closest difference
                dif = key - element
                closestDif = dif
            else:
                dif = element - key
                closestDif = dif
            #sets closest element as the first element
            closestElm = element
        #for the other elements
        #another check to make sure dif is positive
        elif key > element:
            dif = key - element
            #checks if new dif is lest than the closest dif we've already found
            if dif < closestDif:
                #if yes set is as new closest dif
                closestDif = dif
                #add save the element as new closest element
                closestElm = element
        #another check to make sure dif is positive
        elif key <= element:
            dif = element - key
            #checks if new dif is lest than the closest dif we've already found
            if dif < closestDif:
                #if yes set is as new closest dif
                closestDif = dif
                #add save the element as new closest element
                closestElm = element
    return closestElm

def insertElement(A, key):
    #Gives me range of indexes for while loop
    i = len(A) - 1
    #to handle making the array bigger so the A[i+1] index is not out of range
    firstTime = True
    #moves everything bigger than the key to the right
    while i >= 0 and A[i] > key:
        if firstTime:
            #appends the biggest thing to the end to make a bigger array
            A.append(A[i])
            #lowers index to next biggest number
            i = i - 1
            firstTime = False
        else:
            #shifts everything to the right
            A[i+1] = A[i]
            i = i -1
    #if the key is bigger than the largest number in the array, add it to the end
    if key > A[i]:
        A.append(key)
        return A
    #else insert the key into the array in it's new spot
    else:
        A[i+1] = key
    #return array
    return A

def maxSumSubArray(A):
    """Make maxOfSub super small so that things can be greater"""
    maxOfSub = -(2**32)
    """Make max right now 0 until we run through array"""
    maxRightNow = 0
    """starting index keeps track of starting sub array index"""
    startIndex = 0
    """ending index keeps track of ending sub array index"""
    endIndex = 0
    """keep track of index to start a new max sub array"""
    newStart = 0

    #loop through array
    for index in range(len(A)):
        #update the max right now
        maxRightNow += A[index]
        #if the max right now is bigger than the max of the subarray update it
        if maxOfSub < maxRightNow:
            maxOfSub = maxRightNow
            #save where the sub array is starting
            #newStart won't change until this no longer is a max sub array
            startIndex = newStart
            #save new end index
            endIndex = index
        #if the new max right now is smaller than the max of the sub array
        if maxOfSub > maxRightNow:
            #checks if you're at the end of the array
            if index == (len(A) - 1):
                #set maxRightNow to 0 because
                #there are no further max sub array possibilities
                maxRightNow = 0
            #if not at the end of the array
            if index != (len(A) - 1):
                #checks the max of sub array with the next element in the array
                #to see if the subarray is truly not the max
                checkNextMax  = maxRightNow + A[index +1]
            if checkNextMax < maxOfSub:
                #start anew with the max right now
                maxRightNow = 0
                #move the starting index up
                newStart = index + 1
        

    return(startIndex, endIndex)
    
    
            
              
            
