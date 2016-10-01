import queue
import threading
import subprocess

proc = subprocess.Popen(['/usr/bin/git', 'pull'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)


r = proc.stdout.readline()
print(r)
