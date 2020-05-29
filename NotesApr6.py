Hash code:
    Make a key into an int.
    1) Treating bit-map as an itn.
        but if the key is bigger than the bit-map we have to calculate
        - the summation
        -or bitwise xor
    2) Polynomial
        a^n-1x0 + a^n-1x1 + ....
    3) Cyclic-Shift

Compression Function:
    -Divide
        i mod N
    -MAD (Multiphy, Add and Divide)
        [(ai + b) mod p] mod N
        i is what ever the hash function gets you
        p is prime no. > N
        a and b are random numbers that are < p
        a > 0
        N
        this may be more than n
