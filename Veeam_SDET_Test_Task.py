import os
import hashlib
import time
import logging
import sys
import pandas

LOG = 'log.txt'

def log(message):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(LOG, 'a') as f:
        f.write('['+now+']'+message+'\n')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def compare2directories(source, replica):

    filesOfSource = os.listdir(source)
    filesOfReplica = os.listdir(replica)

 
    filesToBeAddedToReplica = []
    
    filesToBeRemovedFromReplica = []
    


    for file1 in filesOfSource:
        number = 0
        for file2 in filesOfReplica:
            if file1 == file2:
                number +=1
        if number == 0:
            filesToBeAddedToReplica.append(file1)
        
            
    for file1 in filesOfReplica:
        num = 0
        for file2 in filesOfSource:
            if file1 == file2:
                num +=1
        if num == 0:
            filesToBeRemovedFromReplica.append(file1)
            

    for fileToBeAdded in filesToBeAddedToReplica:
        if fileToBeAdded:
            os.system('copy ' + source + '\\' + fileToBeAdded + ' ' + replica)        
            log('file coppied: ' + fileToBeAdded)
            logging.info('file coppied: ' + fileToBeAdded)
            
        
    for fileToBeRemoved in filesToBeRemovedFromReplica:   
        if fileToBeRemoved:
            os.remove(replica + '\\' + fileToBeRemoved)                          
            log('file removed: ' + fileToBeRemoved)
            logging.info('file removed: ' + fileToBeRemoved)

while True:
    compare2directories(sys.argv[1], sys.argv[2])
    time.sleep(4)
    
   
   
 #thıs lıne iadded ffromi testbranchı