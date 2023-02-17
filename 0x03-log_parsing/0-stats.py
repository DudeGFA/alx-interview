#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''
from sys import stdin


line_count = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_file_size = 0


try:
    for line in stdin:
        line_count += 1
        split_line = line.split()
        try:
            file_size = int(split_line[-1])
        except Exception:
            continue
        try:
            status_code = int(split_line[-2])
            status_codes[str(status_code)] += 1
        except Exception:
            pass
        total_file_size += file_size
        if line_count % 10 == 0:
            print("File size: " + str(total_file_size))
            for key, value in status_codes.items():
                if value != 0:
                    print("{}: {}".format(key, value))
    print("File size: " + str(total_file_size))
    for key, value in status_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print("File size: " + str(total_file_size))
    for key, value in status_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))
    raise
