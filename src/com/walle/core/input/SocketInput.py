import socket
import threading
import logging
import time
from com.walle.core.input.xmlparser.MessageParser import MessageParser

class SocketInput(threading.Thread):

    def __init__(self, messageParser):
        threading.Thread.__init__(self)
        self.messageParser = messageParser;
	self.ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        self.ServerSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
	self.ServerSocket.bind(("localhost",9999))
	self.ServerSocket.listen(3)
        self.stop=False;

    def close(self):
        self.closingSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        self.closingSocket.connect(("localhost",9999))
        self.closingSocket.send("quit007")
        self.stop=True
        
    def run(self):
        logging.info("SocketInput Started...");

        while self.stop==False:
            logging.info("Waiting for socket connection");
            x=self.ServerSocket.accept()
            SocketInputThread(self.messageParser, x[0]).start();

        self.ServerSocket.shutdown(socket.SHUT_RDWR);
        self.closingSocket.close();
        self.ServerSocket.close();
        logging.info("Exiting socket input thread")

class SocketInputThread(threading.Thread):
    def __init__(self, messageParser, socketInput):
        threading.Thread.__init__(self);
        self.mp=messageParser;
        self.si = socketInput;

    def run(self):
        logging.info("Started Socket Thread");
        ext=False
        while(ext == False):
            message=self.si.recv(1000);
            logging.info("Received message" + message);
            if message=="quit007":                                             
                ext=True                                                             
            self.mp.process(message);
        self.si.close();
        logging.info("Exiting the Socket Thread");   
