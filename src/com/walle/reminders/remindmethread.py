import threading
import time
import logging

from com.walle.core.events.SpeakEvent import SpeakEvent


class remindmethread (threading.Thread):
	def __init__(self, text, waittime, eventQueue):
		threading.Thread.__init__(self)
		self.text = text
		self.waittime = float(waittime)
		self.eventQueue = eventQueue
	def run(self):
		logging.info("Will wait for " + str(self.waittime) + " seconds" );
		time.sleep(self.waittime)
		speakEvent = SpeakEvent(self.text);
		logging.info("Speak Event is Generated for text "+ self.text);
		self.eventQueue.put(speakEvent);
