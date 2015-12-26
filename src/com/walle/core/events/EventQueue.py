import Queue
import logging
from threading import Timer

class EventQueue:
    def __init__(self):
        self.queue = Queue.Queue();
    
    def put(self, event):
        logging.info("Added a event to the queue");
        self.queue.put(event);

    def putTimer(self, event, timerSec):
        logging.info("Will put the event after "+ str(timerSec) +" seconds");
        Timer(float(timerSec), self.put, [event]).start();
            
    def get(self):
        element = self.queue.get();
        self.queue.task_done();        
        return element;
    
    def empty(self):
        return self.queue.empty();
    def qsize(self):
        return self.queue.qsize();
    
