# base code provided by Kevin Ta: https://github.com/kevinta893/581-electronics-examples

import RPi.GPIO as GPIO
import time
import threading

# ring 1
ledPin_1 = 11
buttonPin_1 = 13
motorPin_1 = 15
ring1_on = False

# ring 2
ledPin_2 = 8
buttonPin_2 = 10
motorPin_2 = 12
ring2_on = False

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  
  # setup ring 1
  GPIO.setup(ledPin_1, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(motorPin_1, GPIO.OUT)  
  GPIO.setup(buttonPin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
  # setup ring 1 output
  GPIO.output(ledPin_1, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
  GPIO.output(motorPin_1, GPIO.LOW)
  
  # setup ring 2
  GPIO.setup(ledPin_2, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(motorPin_2, GPIO.OUT)  
  GPIO.setup(buttonPin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
  # setup ring 2 output
  GPIO.output(ledPin_2, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
  GPIO.output(motorPin_2, GPIO.LOW)
  
# thread for receiver ring
# turn LEDs off
def rcvr():
  if ring2_on:
    GPIO.output(ledPin_2, GPIO.LOW)
  
  if ring1_on:
    GPIO.output(ledPin_1, GPIO.LOW)
  
# main loop
def loop():
  while True:
      # ring 1 pushes button
      if (GPIO.input(buttonPin_1) == False) and not (ring2_on or ring1_on):
        print "Ring 1 button pressed!"
        
        # turn on motor of rings 1 and 2 for 0.3s
        GPIO.output(motorPin_2, GPIO.HIGH)
        GPIO.output(motorPin_1, GPIO.HIGH)
        time.sleep(0.3)
        
        # turn on ring 2
        GPIO.output(ledPin_2, GPIO.HIGH)  # led high
        ring2_on = True
        
        # turn on ring 1
        GPIO.output(ledPin_1, GPIO.HIGH)  # led high
        ring1_on = True
        
        # leave LEDs on for 10s
        rcvr_thrd = threading.Thread(target=rcvr, args=(10,))
        rcvr_thrd.start()
      
      # ring 2 pushes button
      if (GPIO.input(buttonPin_2) == False) and not (ring2_on or ring1_on):
        print "Ring 1 button pressed!"
        
        # turn on motor of rings 1 and 2 for 0.3s
        GPIO.output(motorPin_2, GPIO.HIGH)
        GPIO.output(motorPin_1, GPIO.HIGH)
        time.sleep(0.3)
        
        # turn on ring 2
        GPIO.output(ledPin_2, GPIO.HIGH)  # led high
        ring2_on = True
        
        # turn on ring 1
        GPIO.output(ledPin_1, GPIO.HIGH)  # led high
        ring1_on = True
        
        # leave LEDs on for 10s
        rcvr_thrd = threading.Thread(target=rcvr, args=(10,))
        rcvr_thrd.start()

def destroy():
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
