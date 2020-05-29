"""Ways to handle duplicates in the tree
    1) Don't allow them
        -If you discover that a node with key already exists,
        don't add that node again to the tree
    2) Keep a counter
        -if node already exists, increment counter
        -else set it to 1
        class Node:                 
            __init__():                   
                self.count = 1                    
    3) Add node in the tree:
        a) add at leaf level
        b) add as right child of the node with same key

   Map:
       -unique keys are associated with values              mapped to
       -built-in implementation is "dict"
       map M, key k, value v
       M[k]: returns value b associated with key k
           -keyError.__getitem__()
       M[k]=v: add <k,v> in your map
           -replaces previous <k, vl> pair
       del M[k]: removes <k, v> pair
           - key error if k not in m
           - __delitem__()
       iter(M): __iter__()
       k in M: true if k exists, false if not
           __contains__()

    class MapBase(MutableMapping):
        class _Item:
            __slots__ = 'key', 'value' (This saves memory)
            __init__(self, k, v):
                self.key = k
                self.value = v
