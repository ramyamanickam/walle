import threading
import RPi.GPIO as GPIO
from com.walle.core.input.GPIODefinition import PIR_PIN
from com.walle.core.events.Event import MotionSensedEvent

class PersonSensorInput(threading.Thread):
    
    def __init__(self, eventQueue):
        threading.Thread.__init__(self)
        self.eventQueue = eventQueue;
        
        
    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)
        while True:
            if(GPIO.input(PIR_PIN)):
                self.eventQueue.put(MotionSensedEvent());    
                
                
                                                                    