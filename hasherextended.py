#Password Hash Cracker
#Aaron Watkins
#Input Acquired Hash to compare with an input file

import hashlib
import timemod

def main():
    file = input("Please input path of file: ")
    start = timemod.start()
    try:
        with open(file, 'r') as strings:
            print('\nRunning Password Hash Options\n')
            for each_line in strings:
                each_line = each_line.strip()
                try:
                    passmd = hashlib.md5(each_line.encode('utf-8'))
                    passsha1 = hashlib.sha1(each_line.encode('utf-8'))
                    passsha224 = hashlib.sha224(each_line.encode('utf-8'))
                    passsha256 = hashlib.sha256(each_line.encode('utf-8'))
                    passsha384 = hashlib.sha384(each_line.encode('utf-8'))
                    passsha512 = hashlib.sha512(each_line.encode('utf-8'))
                except Exception as err:
                        print(err)
                        print('Please have one string per line')
                print(f'String: {each_line}\n')
                print(f'MD5 Hash: {passmd.hexdigest()}')
                print(f'SHA1 Hash: {passsha1.hexdigest()}')
                print(f'SHA224 Hash: {passsha224.hexdigest()}')
                print(f'SHA256 Hash: {passsha256.hexdigest()}')
                print(f'SHA384 Hash: {passsha384.hexdigest()}')
                print(f'SHA512 Hash: {passsha512.hexdigest()}')
                print('----------------------------------------')
        end = timemod.end()
        timemod.runtime(start, end)
    except FileNotFoundError as err:
        print('File Name Error, please enter valid filename')
        main()


if __name__ == "__main__":
    main()
