# base code provided by Kevin Ta: https://github.com/kevinta893/581-electronics-examples

import RPi.GPIO as GPIO
import time
import threading

class Ring:
  # turn
  ring1_turn = True
  ring2_turn = True
  
  # ring 1
  ledPin_1 = 11
  buttonPin_1 = 13
  motorPin_1 = 15

  # ring 2
  ledPin_2 = 8
  buttonPin_2 = 10
  motorPin_2 = 12

  def setup(self):
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

    # setup ring 1
    GPIO.setup(self.ledPin_1, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(self.motorPin_1, GPIO.OUT)  
    GPIO.setup(self.buttonPin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # setup ring 1 output
    GPIO.output(self.ledPin_1, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
    GPIO.output(self.motorPin_1, GPIO.LOW)

    # setup ring 2
    GPIO.setup(self.ledPin_2, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(self.motorPin_2, GPIO.OUT)  
    GPIO.setup(self.buttonPin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # setup ring 2 output
    GPIO.output(ledPin_2, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
    GPIO.output(motorPin_2, GPIO.LOW)

  # thread for receiver ring
  # turn LEDs off
  def rcvr(self, ring):
    if ring == 1:
      GPIO.output(self.ledPin_2, GPIO.LOW)
    else:
      GPIO.output(self.ledPin_1, GPIO.LOW)

  # main loop
  def loop(self):
    while True:
        # ring 1 pushes button
        if (GPIO.input(self.buttonPin_1) == False) and self.ring1_turn:
          # ring two's turn
          self.ring1_turn = False
          self.ring2_turn = True
          
          print "Ring 1 button pressed!"

          # turn on motor of ring 2 for 0.3s
          GPIO.output(self.motorPin_2, GPIO.HIGH)
          time.sleep(0.3)
          GPIP.output(self.motorPin_2, GPIO.LOW)

          # turn on ring 2
          GPIO.output(self.ledPin_2, GPIO.HIGH)  # led high
          
          # leave LEDs on for 10s
          rcvr_thrd = threading.Thread(target=self.rcvr, args=(10,), kwargs={'ring':1})
          rcvr_thrd.start()

        # ring 2 pushes button
        if (GPIO.input(self.buttonPin_2) == False) and self.ring2_turn:
          # ring one's turn
          self.ring1_turn = True
          self.ring2_turn = False
          
          print "Ring 2 button pressed!"

          # turn on motor of ring 1 for 0.3s
          GPIO.output(self.motorPin_1, GPIO.HIGH)
          time.sleep(0.3)
          GPIP.output(self.motorPin_1, GPIO.LOW)

          # turn on ring 2
          GPIO.output(self.ledPin_2, GPIO.HIGH)  # led high
          
          # leave LEDs on for 10s
          rcvr_thrd = threading.Thread(target=self.rcvr, args=(10,), kwargs={'ring':2})
          rcvr_thrd.start()
          
        # not allowed to push button
        if (GPIO.input(self.buttonPin_1) == False) and not self.ring1_turn:
          # turn on motor of ring 1 for 0.3s
          GPIO.output(self.motorPin_1, GPIO.HIGH)
          time.sleep(0.3)
          GPIP.output(self.motorPin_1, GPIO.LOW)
          
        # not allowed to push button
        if (GPIO.input(self.buttonPin_1) == False) and not self.ring2_turn:
          # turn on motor of ring 1 for 0.3s
          GPIO.output(self.motorPin_1, GPIO.HIGH)
          time.sleep(0.3)
          GPIP.output(self.motorPin_1, GPIO.LOW)

  def destroy():
    GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  
  Ring.setup()
  try:
    Ring.loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    Ring.destroy()
