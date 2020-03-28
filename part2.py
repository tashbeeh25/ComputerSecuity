def encrypt():
    message = input ("Please enter the message: ").lower()#input of message to encrypt
    keyword = input ("Please enter the keyword: ").lower()# input of keyword to encrypt with
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key = ""#empty string which will consist of a combinationof keyword alphabet to make a key
    encrypted=""#empty string which will be populated with the encrypted message
    keyGrid=[]#empty list that will consist of lists to make a key grid
    split_message=[]#empty list that will split the message per 2 letters and insert an x or z where necessary
    i=0#iterator
    message=message.replace(" ","") #Removes white spaces
    while i<len(message):#while the counter is in range of the length of the message
        if  i!=len(message)-1:#if the pointer is not pointing to the last letter
            j=i+1#variable to point to the letter to the right
            if message[i] == message[j]:#if the two letters are the same, add an X at the end of the first letter and increase the iterator by 1
                temp=message[i]+"x"
                split_message.append(temp)
                i=i+1
            else:#else add the two letters to the list and increase the iterator by 2
                temp=message[i]+message[j] 
                split_message.append(temp)
                i=i+2
        else:#if it is the last letter and its not paired, add a Z at the end of it. Increase iterator by 1 so it loops out of the while loop
            temp=message[i]+"z"
            split_message.append(temp)
            i=i+1   
          
    for char in keyword:
        if char in alphabet:
            if char not in key:
                key += char
                
    for char in alphabet:
        if char not in key:
            key += char

    #creating a list of lists with the new key
    keyGrid = [[key[0],key[1],key[2],key[3],key[4]],[key[5],key[6],key[7],key[8],key[9]],[key[10],key[11],key[12],key[13],key[14]],[key[15],key[16],key[17],key[18],key[19]],[key[20],key[21],key[22],key[23],key[24]]]
    for couple in split_message:#for every pair in the split message
        char1=couple[0]                                                                                                                                                           
        char2=couple[1]
        
        for row in range (0,len(keyGrid)):#iterate through keyGrid and find out the position co-ordinates for each letter
            for column in range(0,len(keyGrid[row])):
                if keyGrid[row][column] == char1:
                    char1_ordinates=list(str(column)+str(row))
                if keyGrid[row][column] == char2:
                    char2_ordinates=list(str(column)+str(row))
    #rule1
        if char1_ordinates[0]==char2_ordinates[0]:#if the co-ordinates for the two are in the same column
            if char1_ordinates[1]=="4":#if the letter is on the bottom row, wrap to the top
                char1_ordinates[1]="0"
            else:
                char1_ordinates[1]=str(int(char1_ordinates[1])+1)#move the character down by one space
            if char2_ordinates[0]=="4":#same as above but for the second character
                char2_ordinates[1]="0"
            else:
                char2_ordinates[1]=str(int(char2_ordinates[1])+1)
    #rule2
        elif char1_ordinates[1]==char2_ordinates[1]:# if the co-ordinates for the two are in the same row
            if char1_ordinates[0]=="4":#if the letter is on the right most column, wrap it to the left
                char1_ordinates[0]="0"
            else:
                char1_ordinates[0]=str(int(char1_ordinates[0])+1)#move the character right by one space
            if char2_ordinates[0]=="4":#same as above but for the second character
                char2_ordinates[0]="0"
            else:
                char2_ordinates[0]=str(int(char2_ordinates[0])+1)

    #rule3
        else:#if the characters form a square, swap their columns around
            temp=char1_ordinates[0]
            char1_ordinates[0]=char2_ordinates[0]
            char2_ordinates[0]=temp
        temp=(keyGrid[int(char1_ordinates[1])][int(char1_ordinates[0])])+(keyGrid[int(char2_ordinates[1])][int(char2_ordinates[0])])#getting the appropriate letter with the co-ordinates calculated
        encrypted+=temp

    print(encrypted)

#################################################################################################################################################################################################################            
#################################################################################################################################################################################################################

def decrypt():
    message = input ("Please enter the encrypted message: ").lower()#input of message to encrypt
    keyword = input ("Please enter the keyword: ").lower()# input of keyword to encrypt with
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key = "" #empty string which will consist of a combination of keyword alphabet to make a key
    decrypted="" #empty string which will be populated with the encrypted message
    keyGrid=[] #empty list that will consist of lists to make a key grid
    split_message=[] #empty list that will split the message per 2 letters and insert an x or z where necessary
    i=0 #iterator
    message=message.replace(" ","") #Removes white spaces
    while i<len(message): #while the counter is in range of the length of the message
        if  i!=len(message)-1: #if the pointer is not pointing to the last letter
            j=i+1 #variable to point to the letter to the right
            if message[i] == message[j]:#if the two letters are the same, add an X at the end of the first letter and increase the iterator by 1
                temp=message[i]+"x"
                split_message.append(temp)
                i=i+1
            else:#else add the two letters to the list and increase the iterator by 2
                temp=message[i]+message[j] 
                split_message.append(temp)
                i=i+2
        else:#if it is the last letter and its not paired, add a Z at the end of it. Increase iterator by 1 so it loops out of the while loop
            temp=message[i]+"z"
            split_message.append(temp)
            i=i+1   
          
    for char in keyword:
        if char in alphabet:
            if char not in key:
                key += char
                
    for char in alphabet:
        if char not in key:
            key += char

    #creating a list of lists with the new key
    keyGrid = [[key[0],key[1],key[2],key[3],key[4]],[key[5],key[6],key[7],key[8],key[9]],[key[10],key[11],key[12],key[13],key[14]],[key[15],key[16],key[17],key[18],key[19]],[key[20],key[21],key[22],key[23],key[24]]]
    for couple in split_message:#for every pair in the split message
        char1=couple[0]                                                                                                                                                           
        char2=couple[1]
        
        for row in range (0,len(keyGrid)):#iterate through keyGrid and find out the position co-ordinates for each letter
            for column in range(0,len(keyGrid[row])):
                if keyGrid[row][column] == char1:
                    char1_ordinates=list(str(column)+str(row))
                if keyGrid[row][column] == char2:
                    char2_ordinates=list(str(column)+str(row))
    #rule1
        if char1_ordinates[0]==char2_ordinates[0]:#if the co-ordinates for the two are in the same column
            if char1_ordinates[1]=="0":#if the letter is on the bottom row, wrap to the top
                char1_ordinates[1]="4"
            else:
                char1_ordinates[1]=str(int(char1_ordinates[1])-1)#move the character down by one space
            if char2_ordinates[1]=="0":#same as above but for the second character
                char2_ordinates[1]="4"
            else:
                char2_ordinates[1]=str(int(char2_ordinates[1])-1)
    #rule2
        elif char1_ordinates[1]==char2_ordinates[1]:# if the co-ordinates for the two are in the same row
            if char1_ordinates[0]=="0":#if the letter is on the right most column, wrap it to the left
                char1_ordinates[0]="4"
            else:
                char1_ordinates[0]=str(int(char1_ordinates[0])-1)#move the character right by one space
            if char2_ordinates[0]=="0":#same as above but for the second character
                char2_ordinates[0]="4"
            else:
                char2_ordinates[0]=str(int(char2_ordinates[0])-1)

    #rule3
        else:#if the characters form a square, swap their columns around
            temp=char1_ordinates[0]
            char1_ordinates[0]=char2_ordinates[0]
            char2_ordinates[0]=temp
        temp=(keyGrid[int(char1_ordinates[1])][int(char1_ordinates[0])])+(keyGrid[int(char2_ordinates[1])][int(char2_ordinates[0])])#getting the appropriate letter with the co-ordinates calculated
        decrypted+=temp
    print(decrypted)
            
    

while True:
    UI=input("Would you like to encrypt a messsage, or decrypt an encrypted message? (1,2): ")
    if UI=="1":
        encrypt()
    elif UI=="2":
        decrypt()
    else:
        break
