import logging
import xml.etree.ElementTree as ET
from com.walle.core.events.Event import MoveForwardEvent, MoveStopEvent
from com.walle.core.events.Event import MoveReverseEvent

class MessageParser:
    def __init__(self, queue):
        self.queue = queue;

    def process(self, message):
        doc = ET.fromstring(message);
    
        logging.info("Received the command through socket " + str(doc));
        command = doc.find('name').text;
        logging.info("Received the command through socket " + str(command));
        if(command == "MF"):
            duration = doc.find('duration').text;
            logging.info("Received the duration through socket " + str(duration));            
            
            self.queue.put(MoveForwardEvent());
        
            self.queue.putTimer(MoveStopEvent(),duration);
            logging.info("Creating Move Forward Event for duration " + str(duration));
        
	if(command == "MB"):
            logging.info("Creating Move Backward Event");
            self.queue.put(MoveReverseEvent());
