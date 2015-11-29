from com.walle.core.events.Event import Event
class SpeakEvent( Event ):
    def __init__(self, speakText):
        self.speakText = speakText
        
    def getSpeakText(self):
        return self.speakText;
        
