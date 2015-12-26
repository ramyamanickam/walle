import logging
import xml.etree.ElementTree as ET
from com.walle.core.events.Event import MoveForwardEvent
from com.walle.core.events.Event import MoveReverseEvent

class MessageParser:
    def __init__(self, queue):
        self.queue = queue;

    def process(self, message):
        doc = ET.fromstring(message);
        command=doc.text;
        logging.info("Received the command through socket" + str(command));
        if(command == "MF"):
            logging.info("Creating Move Forward Event");
            self.queue.put(MoveForwardEvent());
	if(command == "MB"):
            logging.info("Creating Move Backward Event");
            self.queue.put(MoveReverseEvent());
