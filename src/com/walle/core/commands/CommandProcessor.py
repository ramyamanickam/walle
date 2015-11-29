from com.walle.reminders.StartReminderAppCommand import StartReminderAppCommand
from com.walle.reminders.StartReminderAppCommandHandler import StartReminderAppCommandHandler



class CommandProcessor:
    def __init__(self, commandQueue, eventQueue):
        self.commandQueue = commandQueue;
        self.reminderCommandHandler = StartReminderAppCommandHandler(eventQueue);
        
    def process(self):
        if(self.commandQueue.qsize() > 0):
            num =  self.commandQueue.qsize()
            for i in range(0, num):
                command = self.commandQueue.get();
                if isinstance(command, StartReminderAppCommand):
                    self.reminderCommandHandler.handle(command);
