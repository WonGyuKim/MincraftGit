import subprocess
import os
import time

directory = 'bedrock-server/'
program = 'bedrock_server.exe'
time = 0

git = subprocess.call('git pull origin master\n', shell=True)

os.chdir(directory)
print(os.getcwd())

process = subprocess.call([program], shell=True)

os.chdir('..')

git = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)

git.stdin.write(bytes('git add .\n', encoding='utf8'))
git.stdin.write(bytes('git commit -m "auto commit in python script"\n', encoding='utf8'))
git.stdin.write(bytes('git push origin master', encoding='utf8'))

