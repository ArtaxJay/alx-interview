#!/usr/bin/python3
'''This script reads lines after another from the STD_IN & computes metrics'''


import sys

network_status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
                       '403': 0, '404': 0, '405': 0, '500': 0}
counter = 0
total_file_size = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            word_size = int(line_list[-1])
            if code in network_status_code.keys():
                network_status_code[code] += 1
            total_file_size += word_size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(network_status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(network_status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
