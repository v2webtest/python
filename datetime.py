import time;

print("DateTime",time.time())

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)