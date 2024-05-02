from socket import *

# method to make connectoin
def conSacn(tgtHost,tgtPort):
    try:
        connskt= socket(AF_INET, SOCK_STREAM)

        connskt.connect((tgtHost, tgtPort))

        print('[+]%d/tcp open' % tgtPort)

        connskt.close()

    except:

        print('[-]%d/tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print('[-] Cant resolve %s' % tgtHost)
        return
    try:
        tgtName= gethostbyaddr(tgtIP)
        print('\n[+] Scan resultof :%s ' % tgtName[0])
    except:
        print('\n[+] Scan resultof : %s ' % tgtIP)

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('Scanning Port: %d ' %tgtPort)
        conSacn(tgtHost,int(tgtPort))


if __name__== '__main__':
   
    # conSacn('216.58.204.142',22)
    portScan('google.com',(80,22))
