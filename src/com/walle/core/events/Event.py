class Event:
    pass;

class CreateReminderEvent( Event ):
    def __init__(self, reminderText, date, category):
        self.reminderText = reminderText;
        self.date = date;
        self.category = category;
        
    def getReminderText(self):
        return self.reminderText;
    
    def getReminderDateTime(self):
        return self.date;
    
    def getCategory(self):
        return self.category;
    
class CreateRemindingEvent( Event ):
    def __init__(self, reminderId):
        self.reminderId = reminderId;
        
    def getReminderId(self):
        return self.reminderId;
    
    
class SpeakEvent( Event ):
    def __init__(self, speakText):
        self.speakText = speakText
        
    def getSpeakText(self):
        return self.speakText;

class SpeakWelcomeWeatherEvent:
    pass;

class MotionSensedEvent:
    pass;

class MoveForwardEvent:
    pass;

class MoveReverseEvent:
    pass;        
