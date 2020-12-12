#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolPumps):
    #
    # Write your code here.
    #
    req = 0
    total = 0
    i = 0

    while i<len(petrolPumps):
        total += petrolPumps[i][0]-petrolPumps[i][1]
        if total<0:
            req -= total
            total = 0
            start = i+1
        i+=1

    if total-req>=0:
        return start
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
