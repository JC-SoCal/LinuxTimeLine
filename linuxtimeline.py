import sys
import os
from subprocess import Popen, PIPE, STDOUT

root = '/home/jc/linuxtimeline_test/'

def rc(command):
  p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
  return p.stdout.read()


f = open('output.csv', 'w')

header = "filename,access,modify,change,birth\n"
f.write(header)

for path, subdir, files in os.walk(root):
  for filename in files:
    command = 'stat ' + os.path.join(path,filename)
    filename = rc(command).split('\n')[0].split('`')[1].rstrip("'")
    #print '1', rc(command).split('\n')[1]
    #print '2', rc(command).split('\n')[2]
    #print '3', rc(command).split('\n')[3]
    access = rc(command).split('\n')[4].split(': ')[1]
    modify = rc(command).split('\n')[5].split(': ')[1]
    change = rc(command).split('\n')[6].split(': ')[1]
    birth = rc(command).split('\n')[7].split(': ')[1]

    line = filename + ',' + access + ',' + modify + ',' + change + ',' + birth + '\n' 
    f.write(line)    

f.close()
#print rc(command)
