import threading
import logging
from com.walle.core.events.Event import CreateReminderEvent
from com.walle.core.events.Event import MotionSensedEvent
from com.walle.core.events.Event import MoveForwardEvent
from com.walle.core.events.Event import MoveReverseEvent

class CommandLineInput(threading.Thread):
	def __init__(self, eventQueue):
		threading.Thread.__init__(self)
		self.eventQueue = eventQueue;
                self.daemon = True
        def stop(self):
                logging.info("Stopping command line input thread");
                thread.exit()
	def run(self):
		logging.info("Starting command line input" );
		exitCommand = False;
		while(exitCommand == False):
                        text = raw_input("Enter the command:");
			if(text.lower() == "reminder"):
				self.reminder_command();
				continue;
			
			if(text.lower() == "quit"):
				exitCommand = True;
				continue
		
			if(text.lower() == "motion"):
				self.eventQueue.put(MotionSensedEvent())
				continue;

			if(text.lower() == "mf"):
                                self.eventQueue.put(MoveForwardEvent())
                                continue;

			if(text.lower() == "mr"):
                                self.eventQueue.put(MoveReverseEvent())
                                continue;
			
			logging.info("Unknown Command")
		logging.info("Exiting command line input .." );	
			
			
			
	def reminder_command(self):
			text = raw_input("Enter the text to be reminded:");
			datetime = raw_input("Enter the datetime to be reminder"); 
			category = raw_input("Enter the category"); 
			event = CreateReminderEvent(text, datetime, category);
			self.eventQueue.put(event);
			
		
