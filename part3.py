import random as rand
import random
import numpy as np
import codecs

r = [0.0] * 2

m1 = 2147483642
a1 = 450
m2 = 2147483423
a2 = 234

y1 = rand.randint(1, m1 - 1)
y2 = rand.randint(1, m2 - 1)

for i in range(0, 2):

    y1 = a1 * y1 % m1
    y2 = a2 * y2 % m2

    x = (y1 - y2) % m1

    if x > 0:
        r[i] = (x / m1)
    elif x < 0:
        r[i] = (x / m1) + 1
    elif x == 0:
        r[i] = (m1 - 1) / m1

print ('Private key for user A: ', r[0])
print ('Private key for user B: ', r[1])

print (" --------------------------------------------------------------------")

a = 3 
q = 353

randNumA = r[0]
randNumB = r[1]

userA = (a**randNumA) % q
userB = (a**randNumB) % q

keyA = (userB**randNumA) % q
print ('Secret key for user A: ',keyA)

keyB = (userA**randNumB) % q
print ('Secret key for user B: ',keyB)

print (" --------------------------------------------------------------------")

f = open("text1.txt", "r")
lines = f.readlines()
for plaintext in lines:
    print ("The text file reads: ", plaintext)
    
key = str(keyA)
mod = 256

# Key Scheduling Algorithm 
def KSA(key):
    key_len = len(key)
    s = list(range(mod))
    j = 0
    for i in range (mod):
        j = (j + s[i] + (key)[i % key_len]) % mod
        s[i], s[j] = s[j], s[i] #swapped
    return s
    

# Pseudo-Random Generation Algorithm
def PRGA(s, n):
    i = j = 0
    key = []
    while n > 0:
        n = n -1
        i = (i + 1) % mod
        j = (j + s[i]) % mod
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % mod]
        key.append(k)
    return key


def preparing_key_array(s):
    return [ord(c) for c in s]

key = preparing_key_array(key)
s = KSA(key)

keystream = np.array(PRGA(s, len(plaintext)))

plaintext = np.array([ord(i) for i in plaintext])

cipher = keystream ^ plaintext #xor two numpy arrays


encrypt = ' '.join('%02x' % i for i in cipher)
print ("Encrypted to: ", encrypt, "->", [chr(c) for c in cipher] )

print (" --------------------------------------------------------------------")


cipher2 = cipher ^ keystream #xor two numpy arrays

decrypt = ' '.join('%02x' % i for i in cipher2)
print ("Decrypted to: ", decrypt, "->",[chr(c) for c in cipher2] )
