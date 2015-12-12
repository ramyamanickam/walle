import logging

class CommandLineOutput:
    def __init__(self, eventQueue):
        self.eventQueue = eventQueue;

    def send_output(self, text):
        logging.warn(text);