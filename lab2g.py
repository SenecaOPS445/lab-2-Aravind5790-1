#!/usr/bin/env python3

# Author: John Doe
# Author ID: 123456789
# Date Created: 2024/05/24

import sys

timer = 3

if len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1

print('blast off!')
