import sys, bot, keyboard
from time import sleep


try:
	BOT = bot.Bot()
	toggle_button = '.'
	enabled = False
	last_state = False
	first_time = True

	print('AntiAFK script started, press "%s" key to start/stop bot.' % toggle_button)

	while True:		
		key_down = keyboard.is_pressed(toggle_button)
		if key_down != last_state:
			last_state = key_down
			if last_state:
				enabled = not enabled
				if enabled and first_time:
					print("\nStarting bot...")
					BOT.start()
					first_time = False
				elif enabled:
					BOT.resume()
				else:
					BOT.pause()
except SystemExit:
	pass
except KeyboardInterrupt:
	sys.exit()