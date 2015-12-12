import logging
from com.walle.db.Reminder import Reminder


def get_reminder_data(reminderId):
    return Reminder("test","Started","speak");
    
def insert_reminder_data(reminder):
    logging.debug("Inserting Reminder data into database" + reminder.getReminderText() + "==>" + reminder.getReminderStatus() + "==>" + reminder.getReminderCategory());
    return 1;
