import subprocess
import time

directory = 'bedrock-server/'
program = 'executor.py'

#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))
#p1.stdin.write(bytes('./' + program + '\n', encoding='utf8'))
#p1.wait()

p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
p1.stdin.write(bytes('./' + program, encoding='utf8'))
p1.communicate()

#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('notepad', encoding='utf8'))

#print('return code : ' + p1.returncode)
#if p1.returncode == 0:
#p2 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#print(p2._waitpid_lock)
#p2.stdin.write(bytes('git branch\n', encoding='utf8'))


