import subprocess
import os
import time

directory = 'bedrock-server/'
program = 'executor.py'
#program = 'bedrock_server.exe'
time = 0

process = subprocess.Popen([program], shell=True)
print(process.returncode)


git = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE, shell=True)

#p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE, shell=True)
#p.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))

#p2 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE, shell=True)
#p.stdin.write(bytes('saps ./' + program + '\n', encoding='utf8'))
#p2.wait()
#while p.poll() is None:
#    time += 1
#    
#    if time % 1000 == 0:
#        p.stdin.write(bytes('git branch\n', encoding='utf8'))

#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))
#p1.stdin.write(bytes('./' + program + '\n', encoding='utf8'))
#p1.wait()

#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('./' + program + '\n', encoding='utf8'))
#p1.communicate()
#p1.wait()

#p1 = subprocess.Popen(['shcm', 'powershell.exe', './' + program], stdin=subprocess.PIPE)
#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('saps powershell.exe ./' + program, encoding='utf8'))
#p1 = subprocess.Popen('./' + program, stdin=subprocess.PIPE)



#while True:
#    print('It\' end!')

#while True:
    

#p1 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p1.stdin.write(bytes('notepad', encoding='utf8'))

#print('return code : ' + p1.returncode)
#if p1.returncode == 0:
#p2 = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#print(p2._waitpid_lock)
#p2.stdin.write(bytes('git branch\n', encoding='utf8'))


