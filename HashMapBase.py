#Assignment 6
#Sari Stissi
#used page 408 of our textbook for help with Item class
#page 416: MAD Method (defs of n, a, b, and p)
#n is the size of the bucket array
#p is a prime number larger than n
#a and b are integers chosen at random from the interval [0, p-1], with a >0
#[(ai+b) mod p] mod N
#page 423

from collections import abc
import random

class HashMapBase(abc.MutableMapping):
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not(self == other)

        def __It__(self, other):
            return self._key < other._key
#---------------------------------------------------------------- 
    def __init__(self, cap=10, prime=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = prime
        self._a = 1 + random.randrange(prime - 1)
        self._b = random.randrange(prime)

    def _hash_function(self, k):
        return(hash(k) * self._a + self._b) % self._prime % len(self._table) 

    def __getitem__(self, k):
        itemJ = self._hash_function(k)
        return self._bucket_getitem(itemJ, k)

    def __setitem__(self, k, v):
        itemJ = self._hash_function(k)
        self._bucket_setitem(itemJ, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        itemJ = self._hash_function(k)
        self._bucket_delitem(itemJ, k)
        self._n -= 1

    def resize(self):
        oldItems = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in oldItems:
            self[k] = v

    def __len__(self):
        return self._n
