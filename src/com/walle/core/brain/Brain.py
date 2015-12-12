from com.walle.core.input.CommandLineInput import CommandLineInput
from com.walle.core.events.EventQueue import EventQueue
from com.walle.core.events.EventProcessor import EventProcessor
from com.walle.core.output.CommandLineOutput import CommandLineOutput
from com.walle.core.output.SpeakerOutput import SpeakerOutput

import logging


queue  = EventQueue();
logging.basicConfig(level=logging.DEBUG)

commandLineput = CommandLineInput(queue);    
commandLineput.start();

commandLineOutput = CommandLineOutput(queue);
speakerOutput = SpeakerOutput(queue);

eventProcessor = EventProcessor(queue, commandLineOutput, speakerOutput);

while True:
    eventProcessor.process();
    
    

    