import threading
import time

exitflag = 0

class Threads (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "Starting " + self.name
        threadlock.acquire()
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name
        threadlock.release()

def print_time(threadName, delay, counter):
    while counter:
        if exitflag:
            threatName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadlock = threading.Lock()
threads = []

#Create new threads
thread1 = Threads(1, "Thread-1", 1)
thread2 = Threads(2, "Thread-2", 2)
thread3 = Threads(3, "Thread-3", 1)

#Add threads to thread list
threads.append(thread1)
threads.append(thread3)

#Assign thread 3 as daemon
thread3.isDaemon()

thread1.start()
thread3.start()

#Wait for all threads to complete
for t in threads:
    t.join()
    

print "Exiting Main Thread"
