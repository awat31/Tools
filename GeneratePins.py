#Code to generate every pin combination.
#To increase/decrease number of digits, add another for loop

pin = 0
f = open('pins.txt', 'w+')
print('Generating Pins...')
for d1 in range(0,10):
    for d2 in range(0,10):
        for d3 in range(0,10):
            for d4 in range(0,10):
                f.write(f'{d1}{d2}{d3}{d4}\n')
f.close()
print('File Created')
