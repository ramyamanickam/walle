import threading
import logging
import RPi.GPIO as GPIO
import time
from com.walle.core.input.GPIODefinition import PIR_PIN
from com.walle.core.events.Event import MotionSensedEvent

class PersonSensorInput(threading.Thread):
    
    def __init__(self, eventQueue):
        threading.Thread.__init__(self)
        self.eventQueue = eventQueue;
        self.ext=False
        
    def close(self):
        self.ext=True    
        
    def run(self):
        logging.info("PersonSensorInput Started...");
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)
        while self.ext==False:
            if(GPIO.input(PIR_PIN)):
                logging.info("Person sensed Event Created");
                self.eventQueue.put(MotionSensedEvent());    
                time.sleep(10);
        GPIO.cleanup()
        logging.info("Exiting person sensor input ..")

                                                                    
