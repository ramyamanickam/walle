import logging
import time
from com.walle.db.Reminder import Reminder
from com.walle.core.events.EventHandler import EventHandler
from com.walle.db.DatabaseData import insert_reminder_data
from com.walle.core.events.Event import CreateRemindingEvent

class ReminderEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue;
        
    def process(self, event):
            logging.info("Handling Reminder Event for" + event.getReminderText() + event.getReminderDateTime());
            reminderModel=Reminder(event.getReminderText(),"Started",event.getCategory());
            reminder_id = insert_reminder_data(reminderModel);
            time.sleep(1)
            self.eventQueue.put(CreateRemindingEvent(reminder_id));
            
