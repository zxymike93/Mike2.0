"""
"""

import io
import subprocess


print('One line at a time:')
p = subprocess.Popen(
    'python3 subprocess_repeater.py',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    p.stdin,
    encoding='utf-8',
    line_buffering=True,
)
stdout = io.TextIOWrapper(
    p.stdout,
    encoding='utf-8',
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())
remainder = p.communicate()[0].decode('utf-8')
print(remainder + '\n')

print('All output at once:')
p = subprocess.Popen(
    'python3 subprocess_repeater.py',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    p.stdin,
    encoding='utf-8',
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
stdin.flush()
output = p.communicate()[0].decode('utf-8')
print(output)
