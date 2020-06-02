## Basic Scripts to get and print the time for you, for
## calculating the length of time scripts run.
## NOTE: All returned values are in Epoch Time, but printed
## in this script in Human-Readable for better presentation

import time as t

def start():
    start = t.time()
    started = t.ctime(start)
    print(f'Start Time: {started}')
    return start

def end():
    end = t.time()
    ended = t.ctime(end)
    print(f'\nEnd Time: {ended}\n')
    return end

def runtime(start, end):
    timediff = round(end-start, 2)  
    print('Time Run:')
    print(f'{timediff} seconds\n')
    return timediff
    
def convert(time):
    converted = t.ctime(time)
    print(f'Epoch Time: {time} = {converted}\n')
    return converted
