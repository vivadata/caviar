import os 

try :
    SOURCE = os.environ['SOURCE']
except KeyError:
    raise KeyError('''
                   ❌ SOURCE environment variable not set, please set it using 
                   export SOURCE=<source_directory>''')

try :
    TARGET = os.environ['TARGET']
except KeyError:
    raise KeyError('''
                     ❌ TARGET environment variable not set, please set it using 
                     export TARGET=<target_directory>''')

STARTING_TAG = os.environ.get('STARTING_TAG',"STRIP_START")
ENDING_TAG = os.environ.get('ENDING_TAG',"STRIP_END")
