import logging
from com.walle.core.events.EventHandler import EventHandler
from com.walle.db.DatabaseData import get_reminder_data

class RemindingEventHandler(EventHandler):
    def __init__(self, speaker, commandLine):
        self.speaker = speaker;
        self.commandLine = commandLine;
        
    def process(self, event):
        logging.info("Handling Reminder Event for" + str(event.getReminderId()));
        reminder = get_reminder_data(event.getReminderId());
        if(reminder.getReminderCategory().lower() =="speak" ):
            self.speaker.speak_text(reminder.getReminderText())
        if(reminder.getReminderCategory().lower() == "write"):
            self.commandLine.send_output(reminder.getReminderText());
            
        
    