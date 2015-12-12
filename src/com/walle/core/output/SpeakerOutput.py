from com.walle.core.events.Event import SpeakEvent

class SpeakerOutput:
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue;

    def speak_text(self, text):
        speakEvent = SpeakEvent(text);
        self.eventQueue.put(speakEvent);