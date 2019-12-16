import subprocess

directory = 'bedrock-server/'
program = 'bedrock_server.exe'
#subprocess.call(['powershell.exe', './' + directory + program])
p = subprocess.Popen('powershell.exe', stdin=subprocess.PIPE)
#out = p.communicate(input='cd ' + directory)
p.stdin.write(['cd', directory])
