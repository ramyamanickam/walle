import logging
from com.walle.core.events.EventHandler import EventHandler
from com.walle.movement import movement

class MoveReverseEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
        is_init=movement.is_initialised()
	if(is_init == False):
            logging.info("Intialising the Movement");
            movement.init();
	movement.move_reverse();
	logging.info("Stopping the movement");
	movement.stop();	
	movement.exit();
        logging.info("Exiting the movement");
