import os
import signal
import subprocess
import sys
import time


p = subprocess.Popen(['python3', 'signal_child.py'])
print('PARENT: Pausing before sending signal..')
sys.stdout.flush()
time.sleep(1)
print('PARENT: Signaling child..')
sys.stdout.flush()
os.kill(p.pid, signal.SIGUSR1)
