data ="""  File: `/root/dirTest/bravo/delta/config.yaml'
  Size: 0           Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d  Inode: 2133310     Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2013-07-09 21:24:02.227793035 -0500
Modify: 2013-07-09 21:24:02.227793035 -0500
Change: 2013-07-09 21:24:02.227793035 -0500
 Birth: -"""



import sys
import os
from subprocess import Popen, PIPE, STDOUT

root = '/root/dirTest/'

def rc(command):
  p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
  return p.stdout.read()

for path, subdir, files in os.walk(root):
  for filename in files:
    command = 'stat ' + os.path.join(path,filename)
    print rc(command).split('\n')[3]
    #for line in rc(command):
    #  print 'x', line