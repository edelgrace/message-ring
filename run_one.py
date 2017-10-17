import RPi.GPIO as GPIO
import time
import threading

class Ring:
	# ring 1
	ledPin_1 = 11
	btnPin_1 = 13
	msg_1 = [0, 0, 0, 0]

	# ring 2
	ledPin_2 = 10
	btnPin_2 = 16
	msg_2 = [0, 0, 0, 0]

	def setup(self):
		GPIO.setmode(GPIO.BOARD)

		# ring 1
		GPIO.setup(ledPin_1, GPIO.OUT)
		GPIO.setup(btnPin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.output(ledPin_1, GPIO.LOW)
		
		# ring 2
		GPIO.setup(ledPin_2, GPIO.OUT)
		GPIO.setup(btnPin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.output(ledPin_2, GPIO.LOW)

	def send_1(self):
		while done_1:
			GPIO.output(ledPin_2, GPIO.HIGH)
			time.sleep(msg_1[0])
			GPIO.output(ledPin_2, GPIO.LOW)

	def loop(self):
		while True:
			# ring 1
			if (GPIO.inout(self.btnPin_1) == False) and count_1 <= 6:
				start_1 = time.time()
				count_1 += 1

