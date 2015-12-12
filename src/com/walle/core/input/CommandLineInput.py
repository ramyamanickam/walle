import threading
import logging
from com.walle.core.events.Event import CreateReminderEvent

class CommandLineInput(threading.Thread):
	def __init__(self, eventQueue):
		threading.Thread.__init__(self)
		self.eventQueue = eventQueue;
		
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
		
			logging.info("Unknown Command")
		logging.info("Exiting command line input" );	
			
			
			
	def reminder_command(self):
			text = raw_input("Enter the text to be reminded:");
			datetime = raw_input("Enter the datetime to be reminder"); 
			category = raw_input("Enter the category"); 
			event = CreateReminderEvent(text, datetime, category);
			self.eventQueue.put(event);
			
		