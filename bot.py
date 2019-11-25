import threading, time
from pynput.keyboard import Key, Controller


def PressKey(key, controller):
	print("[BOT]: Pressing %s" % key)
	controller.press(key)
	time.sleep(15)
	#print("[BOT]: Releasing %s" % key)
	controller.release(key)


class Bot(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.paused = False
		self.pause_condition = threading.Condition(threading.Lock())
		self.keys  = ["w","a","s","d"]
		self.keyboard = Controller()

	def run(self):
		while True:
			with self.pause_condition:
				while self.paused:
					self.pause_condition.wait()

				PressKey(self.keys[0], self.keyboard)
				PressKey(self.keys[2], self.keyboard)

			time.sleep(5)

	def pause(self):
		print("\n[BOT]: Pausing...")
		self.paused = True
		self.pause_condition.acquire()

	def resume(self):
		print("[BOT]: Resuming...\n")
		self.paused = False
		self.pause_condition.notify()
		self.pause_condition.release()