import RPi.GPIO as GPIO
import time
import threading

class Ring:
  # ring 1
  ledPin_1 = 12
  btnPin_1 = 16
  msg_1 = [0, 0, 0, 0]
  count_1 = 0
  start_1 = 0
  end_1 = 0

  # ring 2
  ledPin_2 = 11
  btnPin_2 = 13
  msg_2 = [0, 0, 0, 0]
  count_2 = 0
  start_2 = 0
  end_2 = 0

  def setup(self):
    GPIO.setmode(GPIO.BOARD)

    # ring 1
    GPIO.setup(self.ledPin_1, GPIO.OUT)
    GPIO.setup(self.btnPin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.output(self.ledPin_1, GPIO.LOW)
    
    # ring 2
    GPIO.setup(self.ledPin_2, GPIO.OUT)
    GPIO.setup(self.btnPin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.output(self.ledPin_2, GPIO.LOW)

  def send_1(self):
    while self.count_1 == 0:
      GPIO.output(self.ledPin_1, GPIO.HIGH)
      time.sleep(self.msg_1[0])
      GPIO.output(self.ledPin_1, GPIO.LOW)
      
      
      GPIO.output(self.ledPin_1, GPIO.HIGH)
      time.sleep(self.msg_1[1])
      GPIO.output(self.ledPin_1, GPIO.LOW)
      
      
      GPIO.output(self.ledPin_1, GPIO.HIGH)
      time.sleep(self.msg_1[2])
      GPIO.output(self.ledPin_1, GPIO.LOW)

  def loop(self):
    while True:
      # ring 1 pushes button
      if (GPIO.input(self.btnPin_1) == False) and self.count_1 < 6:
        print("pushed")
        self.start_1 = time.time()
        self.count_1 += 1
        print "Input" + str(GPIO.input(self.btnPin_1))
        print "Count" + str(self.count_1)
            
      elif (GPIO.input(self.btnPin_1) == True) and self.count_1 > 0 and self.count_1 < 6:
        self.end_1 = time.time()
        duration = self.end_1 - self.start_1
        self.msg_1[self.count_1] = duration
              
      elif (GPIO.input(self.btnPin_1) == True) and self.count_1 >= 6:
        self.count_1 = 0
        send = threading.Thread(target=self.send_1)
        send.start()

      if (GPIO.input(self.btnPin_1) == False):        
        print "Count" + str(self.count_1)

  def destroy(self):
    GPIO.cleanup()                  # Release resource
    print "done"

if __name__ == '__main__':     # Program start from here
  
  ring = Ring()
  ring.setup()
  try:
    ring.loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    ring.destroy()
