import logging
from com.walle.core.events.EventHandler import EventHandler
from com.walle.movement import movement

class MoveForwardEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
	is_init=movement.is_initialised()
	if(is_init == False):
		logging.info("Initialising the movement");
		movement.init();
	movement.move_forward();	
	movement.stop();
	logging.info("Stopped the movement");	
	movement.exit();
	logging.info("Exited the movement");
