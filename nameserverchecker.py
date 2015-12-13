from urlparse import urlparse
from threading import Thread
import httplib, sys, os, re, commands

from Queue import Queue

concurrent = 25
success = 0
errors = 0

def doWork():
    while True:
        url = q.get()
        whoisresult = getStatus(url)
        doSomethingWithResult(whoisresult, url)
        q.task_done()

def getStatus(ourl):
    try:
        whoisresult = commands.getoutput("dig ns " + ourl + " +short")
        return whoisresult
    except:
        error = 1
def doSomethingWithResult(whoisresult, domain):
    print domain + ",\"" + whoisresult.replace('\n', ' ') + "\""
q = Queue(concurrent * 2)

for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in open('domains.csv'):  #Location of your CSV containing one domain per line
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
