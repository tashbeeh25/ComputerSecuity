# ComputerSecuity

Task 1 and 2: 

Read a plaintext and a key (user enters his preferred plaintext and the key) and encrypt the plaintext using Playfair Cipher.
Read a Playfair Ciphertext and a key (user enters the Ciphertext and the key) and decrypt the Ciphertext. 

Task 3: 

Suppose that user A wishes to set up a connection with user B and use a secret key to encrypt messages on that connection. The two users, each is going to generates a one-time private key and calculates a public key. These public values, together with global public values for q and α, are stored in some central directory. 
Writen a program in python and address the following requirements.
Generated two random numbers as the one-time private keys for users A and B using combined linear congruential generator considering m1 =
2,147,483,642, a1 = 450, m2 = 2,147,483,423, a2 = 234. For Y0,1, generated a random number between [1, 2,147,483,641] and for Y0,2, generated a random number between [1, 2,147,483,422]. Used modulo operation to generate the random numbers in the range of 0 and 500. (For a new connection, new private keys should be generated)
Using the Diffie-Hellman algorithm and the private keys generated in (a), generated the secret key for users A and B. considered the prime number q = 353 and a primitive root of 353, in this case is α= 3. 
Suppose that user A wishes to send a text file to user B. 
Broke the plaintext into 64 bits blocks and encrypted the last 64 bits block of the plaintext based on RC4 algorithm using the secret key generated previously. Decrypted the encrypted message generated in previously for user B using the secret key. 
