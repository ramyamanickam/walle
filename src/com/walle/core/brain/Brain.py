from com.walle.core.input.CommandLineInput import CommandLineInput
from com.walle.core.input.SocketInput import SocketInput
from com.walle.core.input.PersonSensorInput import PersonSensorInput
from com.walle.core.events.EventQueue import EventQueue
from com.walle.core.events.EventProcessor import EventProcessor
from com.walle.core.output.CommandLineOutput import CommandLineOutput
from com.walle.core.output.SpeakerOutput import SpeakerOutput
from com.walle.core.input.xmlparser.MessageParser import MessageParser
import logging
import sys

queue  = EventQueue();
logging.basicConfig(level=logging.DEBUG)

#commandLineput = CommandLineInput(queue);

#commandLineput.start();
messageParser = MessageParser(queue);

socketInput = SocketInput(messageParser);
socketInput.start();

person_sensor_input = PersonSensorInput(queue);
person_sensor_input.start();

commandLineOutput = CommandLineOutput(queue);
speakerOutput = SpeakerOutput(queue);

eventProcessor = EventProcessor(queue, commandLineOutput, speakerOutput);

try:
    while True:
        eventProcessor.process();
except KeyboardInterrupt:
    socketInput.close();
    person_sensor_input.close()
    sys.exit()
    
    

    
