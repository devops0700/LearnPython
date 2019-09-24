#Importing shutil and time package
import shutil
import time
try:
    print("Copying File")
    #Provide the path to the file which you want to copy
    src = "/Users/manishrana/portcheck.sh"
    #Provide path to the destination folder
    dst = "/Volumes/Data01/devops/logs/"
    #Using shutil's .copy() function which
    #include source and destination path
    shutil.copy(src,dst)
    time.sleep(1)
    print("Successfully Completed")
    time.sleep(0.5)
except:
    print("Unsuccessful!! Error Generated")
    time.sleep(2)