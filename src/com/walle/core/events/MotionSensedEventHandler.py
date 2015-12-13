from com.walle.core.events.EventHandler import EventHandler
from com.walle.core.events.Event import SpeakWelcomeWeatherEvent
from com.walle.core.events.Event import SpeakEvent

class MotionSensedEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue
    
    def process(self, event):
        self.eventQueue.put(SpeakWelcomeWeatherEvent());
        self.eventQueue.put(SpeakEvent("Hello Ramya! How are you?"));
