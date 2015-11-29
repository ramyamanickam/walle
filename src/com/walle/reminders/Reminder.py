import threading
from com.walle.reminders.remindmethread import remindmethread

class Reminder(threading.Thread):
    
    def __init__(self, eventQueue):
        threading.Thread.__init__(self)
        self.eventQueue = eventQueue;
        
    def run(self):
            text = raw_input("Enter the text to be reminded:");
            secToWait = raw_input("Enter the number of seconds to wait:"); 
            try:
                thread1 = remindmethread(text, secToWait, self.eventQueue);
                thread1.start();
            except Exception as ex:
                template = "An exception of type {0} occured. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
