#Password Hash Cracker
#Aaron Watkins
#Input a Hash to compare with a common passwords file
#This version is more memory efficient, it looks at the length of the
#input hash and decides which encoding system to use, rather than
#hashing it using all of the algorithms

import hashlib
import time

def main():
    file = input("Please input path of passwords file: ") #input file
    password = input("Please enter hash to be cracked: ") #input hash
    attempt_counter = 0 # a simple counter of how many password attempts have been done 
    start = time.time() # start a timer
    password_found = False # default holder setting as the program has not found a match
    try:
        with open(file, 'r') as passwords: #open the input file
            print('\nRunning Password Hash Options\n')
            for each_line in passwords: #iterates through each line of the file
                each_line = each_line.strip() # removes all /n at the end of the words
                attempt_counter = attempt_counter + 1 # counter increase
                try:
                    print(f'Attempt: {each_line}') # outputs the currently attempting word
                    
                    #Each of these sections check to see what size the input hash ('password') is, so
                    #the program will hash the words using the correct algorithm.
                    #The section with the matching hash length will hash the current word from the file (each_line)
                    #and check if these two hashes match, if it does not, it moves onto the
                    #next word.
                    #If a match is found, the found flag is set to true, and the program moves to the bottom.

                    #MD5 Hash
                    if len(password) == 32:
                        passmd = hashlib.md5(each_line.encode('utf-8'))
                        if passmd.hexdigest() == password:
                            print(f'\nMD5 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass
                    #SHA1 Hash
                    elif len(password) == 40:
                        passsha1 = hashlib.sha1(each_line.encode('utf-8'))
                        if passsha1.hexdigest() == password:
                            print(f'\nSHA1 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass
                    #SHA224 Hash
                    elif len(password) == 56:
                        passsha224 = hashlib.sha224(each_line.encode('utf-8'))
                        if passsha224.hexdigest() == password:
                            print(f'\nSHA224 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass
                    #SHA256 Hash
                    elif len(password) == 64:
                        passsha256 = hashlib.sha256(each_line.encode('utf-8'))
                        if passsha256.hexdigest() == password:
                            print(f'\nSHA256 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass
                    #SHA284 Hash
                    elif len(password) == 96:
                        passsha384 = hashlib.sha384(each_line.encode('utf-8'))
                        if passsha384.hexdigest() == password:
                            print(f'\nSHA384 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass
                    #SHA512 Hash
                    elif len(password) == 128:
                        passsha512 = hashlib.sha512(each_line.encode('utf-8'))
                        if passsha512.hexdigest() == password:
                            print(f'\nSHA512 Match Found, the password is : {each_line}')
                            end = time.time()
                            password_found = True
                            break
                        else:
                            pass

                except Exception as err:
                        print(err)

        if password_found == False: #If the flag remains false, no match is output
            print('\nNo Match Found')
        end = time.time()
        totaltime = round(end - start, 3)
        print(f'Attempts: {attempt_counter}')
        print(f'Time Elapsed: {totaltime} seconds') 
    except FileNotFoundError as err:
        print('File Name Error, please name file ''common.txt''')


if __name__ == "__main__":
    main()
