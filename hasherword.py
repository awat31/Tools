#Password Hash Comparitor
#Aaron Watkins

import hashlib

def main():
    word = input("Please input string to hash: ")
    passmd = hashlib.md5(word.encode('utf-8'))
    passsha1 = hashlib.sha1(word.encode('utf-8'))
    passsha224 = hashlib.sha224(word.encode('utf-8'))
    passsha256 = hashlib.sha256(word.encode('utf-8'))
    passsha384 = hashlib.sha384(word.encode('utf-8'))
    passsha512 = hashlib.sha512(word.encode('utf-8'))
    print(f'''\nMD5: {passmd.hexdigest()}
SHA1: {passsha1.hexdigest()}
SHA224: {passsha224.hexdigest()}
SHA256: {passsha256.hexdigest()}
SHA384: {passsha384.hexdigest()}
SHA512: {passsha512.hexdigest()}''')
        
if __name__ == "__main__":
    main()
