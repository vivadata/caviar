import os 

SOURCE = os.environ.get('SOURCE',None)
TARGET = os.environ.get('TARGET',None)
STARTING_TAG = os.environ.get('STARTING_TAG',"STRIP_START")
ENDING_TAG = os.environ.get('ENDING_TAG',"STRIP_END")
