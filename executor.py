import subprocess

directory = 'bedrock-server/'
program = 'bedrock_server.exe'

p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE, shell=True)
p.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))
p.stdin.write(bytes('./' + program + '\n', encoding='utf8'))

