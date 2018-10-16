from os import system

print """
URI Fuzzer - a Python script to fuzz servers by sending increasingly long URI's to the target server.

Currently this does not support custom payloads/inputs\n
"""
target = raw_input("Please input the target URI:\n>")
port = raw_input("Input the target port:\n>")
buflen = int(raw_input("Input the buffer length to be added with each iteration:\n>"))
iters = int(raw_input("Input number of iterations to perform:\n>"))
buf = "A"*buflen

for i in range(iters):
    print "\nPerforming iteration number %s of %s" % (i, iters)
    payload = buf * i
    print "Sending URI with buffer length of %s" % len(payload)
    comm = "/usr/bin/curl " + str(target) + ":" + str(port) + "/\"" + str(payload) + "\""
    system(comm)
