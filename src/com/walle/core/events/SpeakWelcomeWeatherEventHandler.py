from com.walle.core.events.EventHandler import EventHandler
from com.walle.weather import weather
from com.walle.core.events.Event import SpeakEvent

class SpeakWelcomeWeatherEventHandler(EventHandler):
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue

    def process(self, event):
        weather_data = weather.welcome_weather('Edinburgh')  
        speak_event = SpeakEvent("It is " + weather_data.get('status') + " day today")
        self.eventQueue.put(speak_event)
