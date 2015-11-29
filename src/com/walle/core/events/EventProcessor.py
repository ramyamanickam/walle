from com.walle.core.events.SpeakEventHandler import SpeakEventHandler
from com.walle.core.events.SpeakEvent import SpeakEvent
import logging

class EventProcessor:
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue;
        self.speakEventHandler = SpeakEventHandler();

    def process(self):
        if(self.eventQueue.qsize() > 0):
            numberOfEvents = self.eventQueue.qsize();
            logging.debug("Total Events Available in the Queue :"+str(numberOfEvents));
            for i in range(0,numberOfEvents):
                logging.debug("Processing Event :"+str(i)); 
                event = self.eventQueue.get();
                if isinstance(event, SpeakEvent):
                    logging.debug("Processing Speak Event");
                    self.speakEventHandler.process(event);
