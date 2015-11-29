from com.walle.reminders.StartReminderAppCommand import StartReminderAppCommand
from com.walle.reminders.Reminder import Reminder

class StartReminderAppCommandHandler:
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue;

    def handle(self, command):
        if isinstance(command,StartReminderAppCommand):
            reminder = Reminder(self.eventQueue);
            reminder.start();
        
