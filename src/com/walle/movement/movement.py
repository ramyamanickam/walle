import time
import sys
import os

from laika import lk
from laika.explorer import exp

ack = [0]
initialised = False
adc_convert_2=235
adc_convert_1=235

def init():
	ret = lk.init()
	if (ret == lk.EXIT_FAILURE):
    		print 'could not open Laika device. Exiting...'
    		sys.exit()
	ret = exp.dout_all(lk.MODULE_ONE, lk.OFF, ack)
        global initialised
        initialised=True
	print("Motor Speed 1:", adc_convert_1)
	print("Motor Speed 2:", adc_convert_2)

def is_initialised():
	return initialised;

def move_forward():
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_1, exp.MOTOR_FORWARD, adc_convert_1, ack)
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_2, exp.MOTOR_FORWARD, adc_convert_2, ack)
  	time.sleep(2);
	
def stop():
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_1, exp.MOTOR_STOP, adc_convert_1, ack)
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_2, exp.MOTOR_STOP, adc_convert_1, ack)
        
def move_reverse():
	ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_1, exp.MOTOR_REVERSE, adc_convert_1, ack)
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_2, exp.MOTOR_REVERSE, adc_convert_2, ack)
	time.sleep(2);

def move_right():        
	ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_1, exp.MOTOR_FORWARD, adc_convert_1, ack)
        ret = exp.motors(lk.MODULE_ONE, exp.MOTOR_2, exp.MOTOR_REVERSE, adc_convert_1, ack)

def exit():
        print "Starting to exit"
	lk.exit()
	initialised=False
        print "Finished exiting"

