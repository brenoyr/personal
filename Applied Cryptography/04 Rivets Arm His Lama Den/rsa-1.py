# Rivets Arm His Lama Den
# Implements a simplistic RSA algorithm with the following characteristics:
# -let's restrict ourselves to "small" numbers
# -write a function that determines if a number is prime
# -write a function that generates all prime numbers within some given range
# -randomly select two of the primes
# -calculate n = p * q
# -write a function that recursively calculates the greatest common divisor of a and b
# -calculate z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
# -write a recursive gcd function
# -write a function that generates all e's and randomly selects one (using isPrime and gcd)
# -write a function that naively calculates d, the modulo inverse of e
# -output the public and private keys
# -write an encrypt function that encrypts message M with the public key to get C
# -write a decrypt function that decrypts ciphertext C with the private key to get M

from sys import stdin
from random import choice

# range for primes p and q
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

# returns all prime numbers within a min/max range
def getPrimes(min, max):
	primes = []

	for n in range(min, max):
		if (isPrime(n)):
			primes.append(n)
	
	return primes

# generates all e's and randomly returns one
def genEs(z):
	es = []

	for e in range(3, z, 2):
		if (isPrime(e) and gcd(z, e) == 1):
			es.append(e)
	
	return es

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

# encrypts a message M with a public key K_pub to get C
def encrypt(M, K_pub):
	# K_pub = (e, n)
	return (M ** K_pub[0]) % K_pub[1]

# decrypts a ciphertext C with a private key K_priv to get M
def decrypt(C, K_priv):
	# K_priv = (d, n)
	return (C ** K_priv[0]) % K_priv[1]

# MAIN
# get input
M = stdin.read().rstrip("\n").split("\n")

# get the primes
primes = getPrimes(MIN_PRIME, MAX_PRIME)
p = choice(primes)
q = choice(primes)
while(q == p):
	q = choice(primes)
print "p = ", p
print "q = ", q

# calculate n and z
n = p * q
print "n = ", n
z = ((p - 1) * (q - 1)) / gcd(p - 1, q - 1)
print "z = ", z

# get the es and select an e
es = genEs(z)
e = choice(es)
print "e = ", e

# calculate d
d = naiveInverse(e, z)
print "d = ", d


# generate the public and private keys
K_pub = (e, n)
K_priv = (d, n)
print "Public key: {}".format(K_pub)
print "Private key: {}".format(K_priv)

# implement RSA for the specified input Ms
for m in M:
	print "--"
	m = int(m)
	c = encrypt(m, K_pub)
	print "m = ", m
	print "c = ", c
	m = decrypt(c, K_priv)
	print "m = ", m
