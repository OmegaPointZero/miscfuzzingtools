from os import system

print """
URI Fuzzer - a Python script to fuzz servers by sending increasingly long URI's to the target server.

Currently this does not support custom payloads/inputs\n
"""
target = raw_input("Please input the target URI:\n>")
port = raw_input("Input the target port:\n>")
start = int(raw_input("Input the buffer length to begin with:\n>"))
end = int(raw_input("Input the buffer length to end on:\n>"))

iters = int(end) - int(start)

for i in range(iters):
    payload = "A"*(int(start) + int(i))
    print "\nSending URI with buffer length of %s" % len(payload)
    comm = "/usr/bin/curl " + str(target) + ":" + str(port) + "/\"" + str(payload) + "\""
    system(comm)

