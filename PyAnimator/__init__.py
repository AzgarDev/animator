import os, sys, time
from colorama import Fore, init, AnsiToWin32
import threading

def animation2(message, tempo, cycle, xx, xy, dots=None):
	sys.stderr.flush()
	os.system("cls")
	sys.stderr.flush()
	init(autoreset=True)
	init(wrap=False)
	stream = AnsiToWin32(sys.stderr).stream
	colors = dict(Fore.__dict__.items())
	dot = '.'
	sys.stderr.flush()

	if dots:
		sys.stderr.flush()
		for color, i in zip(colors.keys(), range(tempo)):
			sys.stderr.write("\x1b7\x1b\x1b[F\x1b[F[%d;%df%s\x1b8" % (xx, xy, colors[color] + message + dot))
			sys.stderr.flush()
			time.sleep(cycle)
			dot = dot + '.'
		sys.stderr.flush()
	else:
		sys.stderr.flush()
		for color, i in zip(colors.keys(), range(tempo)):
			sys.stderr.write("\x1b7\x1b\x1b[F\x1b[F[%d;%df%s\x1b8" % (xx, xy, colors[color] + message))
			sys.stderr.flush()
			time.sleep(cycle)
		sys.stderr.flush()

def animation(message, tempo, cycle, xx, xy, dots=None):
	if dots == True:
		sys.stderr.flush()
		taskjrhkajshurhuuuuwuuauslkjrljksaf = threading.Thread(target=animation2, args=(message, tempo, cycle, xx, xy), kwargs={'dots': True})
		taskjrhkajshurhuuuuwuuauslkjrljksaf.start()
		os.system("cls")
		sys.stderr.flush()
		time.sleep(0.10)
		os.system("cls")
	else:
		sys.stderr.flush()
		taskjrhkajshurhuuuuwuuauslkjrljksaf = threading.Thread(target=animation2, args=(message, tempo, cycle, xx, xy), kwargs={'dots': False})
		taskjrhkajshurhuuuuwuuauslkjrljksaf.start()
		os.system("cls")
		sys.stderr.flush()
		os.system("cls")
