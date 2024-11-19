# TEST PROGRAM
# this is for demonstration of microservice only
# simulates user pressing "BUY" on vending machine keypad

import time

while True:
    item_code = input('Select a button on the vending machine: ')
    with open('file.txt', 'w') as fout:
        fout.write(item_code)

    time.sleep(10)

    with open('file.txt', 'r') as fin:
        line = fin.readline()
        if line.isdigit():
            print(f'Your animation number is: {line}')