"""
interaction.py 的子进程
"""

import sys


sys.stderr.write('repeater.py: starting..\n')
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    sys.stderr.flush()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('repeater.py: exiting..\n')
sys.stderr.flush()
