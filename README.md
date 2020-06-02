# Tools
Hashing Code, Pin Generators Etc

Pin Generator - Generates every combination of pin from 0000 to 9999, for a phone pin brute force

WPS Pin Generator - Generates all Pins between 00000000 and 99999999. For a WPS pin brute force, this output will take up a lot of space.

TimeMod - This is a useful python module for generating runtime for scripts, use start = timemod.start() to begin, end = timemod.end() to finish, then timemod.runtime(start, end) to generate the time between, and how long the program has run.

Hasherword will simply prompt you for a word then hash it in multiple hashes for you.
Hasherextended will take in a file or list and hash each word for you. I wouldn't recommend more than 10 as the output will pile up quickly.

Comparator - Will ask for two files, one a large dictionary/main file and a file containing target words, it will then see if the target words make an appearence in the larger file, and return the ones that do. Useful if you have a large set of hashes and want to look for specific ones within it.
