import os
from com.walle.core.events.EventHandler import EventHandler

class SpeakEventHandler(EventHandler):
    def process(self, event):
            print(event.getSpeakText());
            os.system("espeak " + event.getSpeakText());
