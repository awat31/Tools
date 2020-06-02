# Tools
Tools I've written to achieve a purpose or for the novelty of writing them.

Pin Generator - Generates every combination of pin from 0000 to 9999, for a phone pin brute force

WPS Pin Generator - Generates all Pins between 00000000 and 99999999. For a WPS pin brute force, this output will take up a lot of space.

TimeMod - This is a useful python module for generating runtime for scripts, use start = timemod.start() to begin, end = timemod.end() to finish, then timemod.runtime(start, end) to generate the time between, and how long the program has run.

Hasherword will simply prompt you for a word then hash it in multiple hashes for you.
Hasherextended will take in a file or list and hash each word for you. I wouldn't recommend more than 10 as the output will pile up quickly.

Comparator - Will ask for two files, one a large dictionary/main file and a file containing target words, it will then go through each word in the targets file to see if the target words make an appearence in the larger file, and return the ones that do. Useful if you have a large set of hashes and want to see if multiple specific ones are within it.

Password Cracker will take in a hash and a dictionary file with a list of words, it will then hash each word in turn and compare it to the input hash. If it gets a match it will display that it has found the password.
Password cracker will do this behind the scenes and display it's conculsion, password cracker legacy will display each option as it runs through so it can be seen on screen. This is much slower.

Note many of these tools reference the timemod module for displaying the time they took, so will need those lines removed or timemod downloaded aswell. If copied into \Python\Python37-32\Lib folder it can be called by any script.
