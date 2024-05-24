#!/usr/bin/env python3

# Author: Aravind Ravi Kumar
# Author ID: 118188200
# Date Created: 2024/05/24

import sys

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' timer')
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer =timer - 1
    
print('blast off!')
