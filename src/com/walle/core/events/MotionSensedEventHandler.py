from com.walle.core.events.EventHandler import EventHandler
from com.walle.core.events.Event import SpeakWelcomeWeatherEvent

class MotionSensedEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
        self.eventQueue.put(SpeakWelcomeWeatherEvent());
