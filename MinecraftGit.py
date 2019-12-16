import subprocess
import time

directory = 'bedrock-server/'
program = 'bedrock_server.exe'

p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
p.stdin.write(bytes('cd ' + directory + '\n', encoding='utf8'))
p.stdin.flush()

p.stdin.write(bytes('./' + program + '\n', encoding='utf8'))
p.stdin.flush()

#p.communicate(bytes('cd ' + directory, encoding='utf8'))

#p = subprocess.call('powershell.exe', stdin=subprocess.PIPE)



#p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#p.communicate(bytes('./' + program, encoding='utf8'))

#p.stdin.write(bytearray(['cd ' + directory]))
#p.communicate()
#out = p.communicate(input='cd ' + directory)
#p.stdin.write(['cd', directory])
