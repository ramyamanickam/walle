

class Reminder:
    def __init__(self, reminderText, reminderStatus, reminderCategory):
        self.reminderText = reminderText;
        self.reminderStatus = reminderStatus;
        self.reminderCategory = reminderCategory;
    
    def getReminderText(self):
        return self.reminderText;
    
    def getReminderStatus(self):
        return self.reminderStatus;
    
    def getReminderCategory(self):
        return self.reminderCategory;
    
class ReminderCategory:
    def __init__(self, reminderCateogryId, categoryName, categoryOutputType):
        self.reminderCateogryId = reminderCateogryId;
        self.categoryName = categoryName;
        self.categoryOutputType = categoryOutputType;
        
        
    def getReminderCateogryId(self):
        return self.reminderCateogryId;
    
    def getCategoryName(self):
        return self.reminderText;
