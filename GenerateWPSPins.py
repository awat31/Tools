#Code to generate every pin combination.
#To increase/decrease number of digits, add another for loop

pin = 0
f = open('WPSpins.txt', 'w+')
print('Generating Combinations...')
for d1 in range(0,10):
    for d2 in range(0,10):
        for d3 in range(0,10):
            for d4 in range(0,10):
                for d5 in range(0,10):
                    for d6 in range(0,10):
                        for d7 in range(0,10):
                            for d8 in range(0,10):
                                f.write(f'{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}\n')
                                
f.close()
print('File Created')

