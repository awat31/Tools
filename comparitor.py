## Program for comparing two string lists to see if there are matching entries
## in both.
## Could be used for hash comparisons.
## Aaron Watkins
## 02/06/2020

import time
import timemod

def main():
    searchFile = input('Input Path to File Containing Strings to Search: ')
    targetFile = input('Input Path to File Containing Target Strings: ')

    comparisons = 0
    matchCounter = 0
    matches = []
    matchFound = False
    start = timemod.start()

    try:
        #Goes through each line of the target file.
        #This comes first as it is more efficient.
        print(f'Comparing {searchFile} with {targetFile}...\n')
        with open(targetFile, 'r') as targets:
                for each_line in targets:
                    targetstr = each_line.strip()

                    #This goes through each line in the strings list file
                    #It increases the record of number of comparisons by 1
                    with open(searchFile, 'r') as searches:
                        for each_line in searches:
                            searchstr = each_line.strip()
                            comparisons = comparisons + 1
                            
                            #This compares the current target line with the current search line to see if they match
                            #If they do, the match is recorded in the matches list and the program moves onto the next target
                            #if they don't, the program moves on to the next string to compare the target to. 
                            if  targetstr == searchstr:
                                matchCounter = matchCounter + 1
                                matchFound = True
                                matches.append(searchstr)
                                break
                            else:
                                continue
                
    except FileNotFoundError as err:
        print('File Not Found - Please Enter a Valid File Path\n')
        main()

    #Outputs  - If there are more than 100 matches, for ease of view, the program will write the results to a
    #file rather than displaying them all.
    if matchFound == False:
         print('No Matches Found\n')

    else:
        print(f'Matches Found!\n')
        print(f'{matchCounter} Total Match/es: ')
        if matchCounter < 100:
            print(*matches, sep =', ')
            print('')
        else:
            f = open('MatchingStrings.txt', 'w+')
            for line in matches:
                f.write(f'{line}\n')
            f.close()
            print('\nMore then 100 matches. Output Written to results.txt file.\n')
            

    end = timemod.end()
    totaltime = timemod.runtime(start, end)
    print(f'Comparisons Run: {comparisons}')
    
    

if __name__ == "__main__":
    main()
