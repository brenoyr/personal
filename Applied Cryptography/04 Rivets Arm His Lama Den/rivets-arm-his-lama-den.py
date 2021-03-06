#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Rivets Arm His Lama Den                 #
#   Due Date:   04/17/2020                              #
#   Comments:   Python 2.7.17                           #
#                                                       #
#               Works with ciphertexts 1-3.             #
#########################################################

# Rivets Arm His Lama Den
# Implements a simplistic RSA algorithm with the following characteristics:
# -expect input to contain the public key on the first line and a comma separated list of numbers representing encrypted values on the second line
# -the input provides n and e
# -write a function that determines if a number is prime
# -write a function that factors a number into the product of two primes
# -write a function that recursively calculates the greatest common divisor of a and b
# -write a function that naively calculates d, the modulo inverse of e
# -write a decrypt function that decrypts ciphertext C with the private key to get M
# -factor n as the product of two primes, p and q
# -calculate z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
# -calculate d as the inverse modulo of e
# -output the public and private keys
# -decrypt each value from the input using the private key to generate a valid ASCII character
# -rebuild the original message

from sys import stdin, stdout, stderr

MIN_PRIME = 100
MAX_PRIME = 999

# determines if a given number is prime
def isPrime(n):
	if (n % 2 == 0):
		return False
	
	for i in range(3, int(n ** 0.5 +1), 2):
		if (n % i == 0):
			return False
	
	return True

# factors a number n into the product of two primes
def factor(n):
	for i in range(3, int(n ** 0.5 + 1), 2):
		if (n % i == 0 and isPrime(i) and isPrime(n / i)):
			return i, n / i
	
	return None

# recursively returns the greatest common divisor of a and b
def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a % b)

# naively calculates the inverse modulo of e and z
def naiveInverse(e, z):
	d = 0

	while (d < z):
		if ((e * d) % z == 1):
			return d
		d += 1

# decrypts a ciphertext C with a private key K_priv to get M
def decrypt(C, K_priv):
	# K_priv = (d, n)
	return (C ** K_priv[0]) % K_priv[1]

# generates all e's in the form 2^n + 1
def genEs(z):
    es = []
    e = 3       # first prime > 2
    exp = 1     # exponent

    while e < z:
        es.append(e)
        exp *= 2
        e = ((2 ** exp) + 1)
    
    return es

# MAIN
# get input
ciphertext = stdin.read().rstrip("\n").split("\n")

# grab the public key and ciphertext values
n = int(ciphertext[0])
C = ciphertext[1].split(",")

# factor n into p and q
p, q = factor(n)
print "p={}, q={}".format(p, q)
print "n={}".format(n)

# calculate z
z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
print "z={}".format(z)

# get the es (in the form of 2^n + 1)
es = genEs(z)

# naive method:
for i in range (0, len(es)):
    e = es[i]
    print "--"
    print "Trying e={}".format(e)

    # calculate d
    d = naiveInverse(e, z)

    if d == None:
        print "No d found"
        continue    # go to the next e

    print "d={}".format(d)

    # generate the public key
    K_pub = (e, n)
    print "Public key: {}".format(K_pub)

    # generate the private key
    K_priv = (d, n)
    print "Private key: {}".format(K_priv)

    stdout.flush()

    # implement RSA for the specified input Cs
    M = ""
    for c in C:
        m = decrypt(int(c), K_priv)
        try:
            M += chr(m)
            stdout.write(chr(m))
            stdout.flush()
        except:
            print "ERROR: invalid plaintext."
            break

    print
