import Queue
import logging

class CommandQueue:
    def __init__(self):
        self.queue = Queue.Queue();
    
    def put(self, command):
        logging.info("Added a command to the queue");
        self.queue.put(command);

    def get(self):
        element = self.queue.get();
        self.queue.task_done();        
        return element;
    
    def empty(self):
        return self.queue.empty();

    def qsize(self):
        return self.queue.qsize();


