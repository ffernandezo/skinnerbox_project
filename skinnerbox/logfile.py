import datetime

class LogFile:
    def __init__(self,filename):
        self.filename = filename
    
    def log_event(self,event):
        now = datetime.datetime.now()
        timp = now.strftime("%y/%m/%d-%H:%M:%S") + " "+ event
        print(timp)
        with open(self.filename, "a") as file:
          file.write(timp +chr(10))
     