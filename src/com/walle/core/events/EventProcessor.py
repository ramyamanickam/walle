import logging

from com.walle.core.events.SpeakEventHandler import SpeakEventHandler
from com.walle.core.events.Event import SpeakEvent
from com.walle.core.events.Event import CreateReminderEvent
from com.walle.core.events.Event import CreateRemindingEvent
from com.walle.core.events.Event import MotionSensedEvent
from com.walle.core.events.Event import SpeakWelcomeWeatherEvent
from com.walle.core.events.Event import MoveForwardEvent
from com.walle.core.events.Event import MoveReverseEvent
from com.walle.core.events.Event import MoveStopEvent
from com.walle.core.events.MoveForwardEventHandler import MoveForwardEventHandler
from com.walle.core.events.MoveReverseEventHandler import MoveReverseEventHandler
from com.walle.core.events.MoveStopEventHandler import MoveStopEventHandler
from com.walle.core.events.ReminderEventHandler import ReminderEventHandler
from com.walle.core.events.RemindingEventHandler import RemindingEventHandler
from com.walle.core.events.MotionSensedEventHandler import MotionSensedEventHandler
from com.walle.core.events.SpeakWelcomeWeatherEventHandler import SpeakWelcomeWeatherEventHandler


class EventProcessor:
    def __init__(self, eventQueue, commandLineOutput, speakOutput):
        self.eventQueue = eventQueue;
        self.commandLineOutput =  commandLineOutput;
        self.speakOutput = speakOutput;

        self.speakEventHandler = SpeakEventHandler();
        self.reminderEventHandler = ReminderEventHandler(self.eventQueue);
        self.remindingEventHandler = RemindingEventHandler(self.speakOutput, self.commandLineOutput);
        self.motionSensedEventHandler = MotionSensedEventHandler(self.eventQueue);
        self.speakWelcomeWeatherEventHandler = SpeakWelcomeWeatherEventHandler(self.eventQueue);
	self.moveForwardEventHandler = MoveForwardEventHandler(self.eventQueue);
	self.moveReverseEventHandler = MoveReverseEventHandler(self.eventQueue);
        self.moveStopEventHandler = MoveStopEventHandler(self.eventQueue);
      
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
                if isinstance(event, MotionSensedEvent):
                    logging.debug("Processing Create Motion Sensed Event");
                    self.motionSensedEventHandler.process(event);    
                if isinstance(event, SpeakWelcomeWeatherEvent):
                    logging.debug("Processing Speak Welcome Weather Event");
                    self.speakWelcomeWeatherEventHandler.process(event);    
		if isinstance(event, MoveForwardEvent):
                    logging.debug("Processing Move Forward Event");
                    self.moveForwardEventHandler.process(event); 
		if isinstance(event, MoveReverseEvent):
                    logging.debug("Processing Move Reverse Event");
                    self.moveReverseEventHandler.process(event);  
                if isinstance(event, MoveStopEvent):
                    logging.debug("Processing Move Stop Event");
                    self.moveStopEventHandler.process(event);
