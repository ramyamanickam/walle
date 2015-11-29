from com.walle.core.events.EventQueue import EventQueue
from com.walle.core.commands.CommandQueue import CommandQueue
from com.walle.core.events.EventProcessor import EventProcessor
from com.walle.core.commands.CommandProcessor import CommandProcessor

from com.walle.reminders.StartReminderAppCommand import StartReminderAppCommand
import logging

#Initialise  
queue  = EventQueue();
commandQueue =  CommandQueue();
eventProcessor = EventProcessor(queue);
commandProcessor = CommandProcessor(commandQueue, queue);
logging.basicConfig(level=logging.DEBUG)
#Call events to run -- testing for now
setReminder=1;

while True:

    if setReminder==1:
        logging.debug("Starting Reminder thread now ... ")
        setReminder=0;
        command = StartReminderAppCommand();
        commandQueue.put(command);
    else:
           
            eventProcessor.process();
            commandProcessor.process();
