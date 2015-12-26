import logging
from com.walle.core.events.EventHandler import EventHandler
from com.walle.movement import movement

class MoveStopEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
        
        logging.info("Stopping the Movement");
	movement.stop();
	
        
