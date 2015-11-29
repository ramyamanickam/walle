import os
from com.walle.core.events.EventHandler import EventHandler

class SpeakEventHandler(EventHandler):
    def process(self, event):
            os.system("espeak " + event.getSpeakText());
