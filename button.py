import RPi.GPIO as GPIO
import time
import sys

ledPin_1 = 12
ledPin_2 = 22

buttonPin_1 = 19
buttonPin_2 = 23

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  
  GPIO.setup(ledPin_1, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(ledPin_2, GPIO.OUT)   # Set LedPin's mode is output
  
  GPIO.setup(buttonPin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonPin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
  GPIO.output(ledPin_1, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
  GPIO.output(ledPin_2, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

def loop():
  while True:
      if(GPIO.input(buttonPin_1) == False):
        print "Button 1 pressed!"

        GPIO.output(ledPin_2, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(ledPin_2, GPIO.LOW) # led off
        
      if(GPIO.input(buttonPin_2) == False):
        print "Button 2 pressed!"

        GPIO.output(ledPin_1, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(ledPin_1, GPIO.LOW) # led off

def destroy():
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
    sys.exit()
