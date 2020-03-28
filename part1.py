cipherText = 'te td fyvyzhy szh pqqpnetgp esp nlpdlc ntaspc hld le esp etxp, mfe te td wtvpwj ez slgp mppy cpldzylmwj dpnfcp, yze wplde mpnlfdp xzde zq nlpdlcd pypxtpd hzfwo slgp mppy twwtepclep lyo zespcd hzfwo slgp lddfxpo esle esp xpddlrpd hpcp hcteepy ty ly fyvyzhy qzcptry wlyrflrp. '
alphabet = 'abcdefghijklmnopkrstuvwxyz'

## loop for possible keys 
for key in range(len(alphabet)):

    ## blank string to store the plaintext
    plainText = ''

    
    for letter in cipherText:
        
        if letter in alphabet:
            
            number = alphabet.find(letter)
            number = number - key

            if number < 0:
                number = number + len(alphabet)

            plainText = plainText + alphabet[number]
            
        else:
            plainText = plainText + letter

    print('Key:',key)
    print (plainText)
