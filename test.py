import pexpect
import subprocess

"""
proc = subprocess.Popen(['/usr/bin/git', 'push'], stdout=subprocess.PIPE)

stdout_value = proc.communicate()[0].decode("utf-8")
if stdout_value == "" :
	print("ya rien dedans :( ")
else :
	print("ya un truc " + stdout_value)
"""

child = pexpect.spawn ("git push")
child.expect("Username for .*")
print(child.before.decode("utf-8"))
child.send("FlorianDoublet")
print(child.read())
child.expect("Password")
print(child.before)
child.send("Tu le sauras pas")
print(" last " + child.after.decode("utf-8"))
