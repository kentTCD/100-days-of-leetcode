## How to Use
# on comandline, use this with 2 or 3 arguments

## Examples
# python add_file.py Day15 "1342. Number of Steps to Reduce a Number to Zero" "{whole your code (Not Needed)}"
# or
# python add_file.py Day15 "1342. Number of Steps to Reduce a Number to Zero"

import os
import sys

argv = sys.argv

os.makedirs('codes/' + argv[1], exist_ok=True)
file_name = argv[2].replace(' ', '-').replace('.', '') + '.py'
file_content = '' if len(argv) < 4 else argv[3]
f = open('codes/' + argv[1] + '/' + file_name, 'w')
f.write(file_content)
f.close()

bar = ' ----------------- '
print(bar + "Created: " + argv[1] + '/' + file_name + bar)