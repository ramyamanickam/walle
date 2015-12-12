import logging

from com.walle.core.events.SpeakEventHandler import SpeakEventHandler
from com.walle.core.events.Event import SpeakEvent
from com.walle.core.events.Event import CreateReminderEvent
from com.walle.core.events.Event import CreateRemindingEvent
from com.walle.core.events.ReminderEventHandler import ReminderEventHandler
from com.walle.core.events.RemindingEventHandler import RemindingEventHandler

class EventProcessor:
    def __init__(self, eventQueue, commandLineOutput, speakOutput):
        self.eventQueue = eventQueue;
        self.commandLineOutput =  commandLineOutput;
        self.speakOutput = speakOutput;

        self.speakEventHandler = SpeakEventHandler();
        self.reminderEventHandler = ReminderEventHandler(self.eventQueue);
        self.remindingEventHandler = RemindingEventHandler(self.speakOutput, self.commandLineOutput);
      
    def process(self):
        if(self.eventQueue.qsize() > 0):
            numberOfEvents = self.eventQueue.qsize();
            logging.debug("Total Events Available in the Queue :"+str(numberOfEvents));
            for i in range(0,numberOfEvents):
                event = self.eventQueue.get();
                if isinstance(event, SpeakEvent):
                    logging.debug("Processing Speak Event");
                    self.speakEventHandler.process(event);
                if isinstance(event, CreateReminderEvent):
                    logging.debug("Processing Create Reminder Event");
                    self.reminderEventHandler.process(event);
                if isinstance(event, CreateRemindingEvent):
                    logging.debug("Processing Create Reminding Event");
                    self.remindingEventHandler.process(event);    
                    