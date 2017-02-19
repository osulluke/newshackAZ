from time import sleep
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import csv

########## CODE FOR PINS ##########

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 21
GPIO.setup(INPUT_PIN, GPIO.IN, GPIO.PUD_DOWN)

########## END ##########

### CREATE DATA FILE ###

DataFile = 'data.csv'

########## Define function to read data #####

def readMotionData():
    while True:
        motionStatus = "..."
        # get a date/time string:
        now = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
        # take reading
        current_reading = GPIO.input(INPUT_PIN)
    
        # current_reading will be a 1 or 0. 1 means motion
        if (current_reading == 1):
            motionStatus = "MOTION DETECTED"
            print motionStatus
        else:
            print motionStatus

        myCsv = open(DataFile, 'a')
        csvWriter = csv.writer(myCsv)
        csvWriter.writerow([now, motionStatus])
        myCsv.close()
    
        # wait two seconds:
        sleep(2)

########## END ##########


### check csv for a header ###

def check_header():
    # open csv for reading
    try:
        mycsv = open(DataFile, 'rb')
    except:
        # open csv for writing:
        mycsv = open(DataFile, 'wb')
    # make the csv writer object
    writer = csv.writer(mycsv)
    # write the header row
    writer.writerow(['date', 'motion status'])

check_header()
while True:
    readMotionData()
