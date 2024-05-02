#!/usr/bin/python3
import sys

"""
A script that reads stdin line by line and computes the metrics
"""


def main():
    """Reads lines from stdin"""
    totalFileSize = 0
    statusCodes = {}

    try:
        for idx, line in enumerate(sys.stdin, start=1):
            fileSize = int(line.split()[5])
            statusCode = line.split()[4]

            totalFileSize += fileSize
            if statusCode in statusCodes:
                statusCodes[statusCode] += 1
            else:
                statusCodes[statusCode] = 1
            if ((idx + 1) % 10 == 0):
                print(f'File size: {totalFileSize}')
                sortedCodes = sorted(statusCodes.items())
                for key, value in sortedCodes:
                    print(f'{key}: {value}')
    except KeyboardInterrupt:
        print(f'File size: {totalFileSize}')
        sortedCodes = sorted(statusCodes.items())
        for key, value in sortedCodes:
            print(f'{key}: {value}')


if __name__ == '__main__':
    main()
