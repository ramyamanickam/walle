import logging
from com.walle.core.events.EventHandler import EventHandler
from com.walle.movement import movement

class MoveStopEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
        is_init=movement.is_initialised()
	if(is_init == True ):
            movement.stop();
        else:
            logging.info("Movement is not initialised");
        
	
        
