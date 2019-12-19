import subprocess
import os

directory = 'bedrock-server/'
program = 'bedrock_server.exe'

#os.chdir(directory)
#print(os.getcwd())

p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE, shell=True)
p.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))
p.stdin.write(bytes('saps ./' + program + '\n', encoding='utf8'))

