# Item Code Lookup microservice for Vending Machine Simulator
#
# Receives an item code from vending machine,
# and returns the corresponding animation code

import time

while True:
    time.sleep(10)

    with open('file.txt', 'r') as fin:
        item_code = fin.readline()
        if not item_code:
            print('NaN')
        else:
            with open('file.txt', 'w') as fout:
                if item_code == 'A1':
                    fout.write('1')
                elif item_code == 'A2':
                    fout.write('2')
                elif item_code == 'A3':
                    fout.write('3')
                elif item_code == 'B1':
                    fout.write('4')
                elif item_code == 'B2':
                    fout.write('5')
                elif item_code == 'B3':
                    fout.write('6')
                elif item_code == 'C1':
                    fout.write('7')
                elif item_code == 'C2':
                    fout.write('8')
                elif item_code == 'C3':
                    fout.write('9')

        time.sleep(10)






