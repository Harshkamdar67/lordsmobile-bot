

from _polling import *


REPEAT_MAX = 5;
REPEAT_VAL = REPEAT_MAX;

SETTINGS = [
	'WINDOW_TOP_LEFT',
	'WINDOW_BOTTOM_RIGHT', 
	'MAGNIFIER_ICON', 
	'COORDINATE_X', 
	'COORDINATE_Y', 
	'COORDINATE_GO',
	'CALCULATOR[1]',
	'CALCULATOR[9]'
	]

HEADER = '#======='
FOOTER = '#======='
def _setupWindow():
	WINDOW_TOP_LEFT = _setSetting('WINDOW_TOP_LEFT')
	WINDOW_BOTTOM_RIGHT = _setSetting('WINDOW_BOTTOM_RIGHT')

def _string_comprehension(l):
	return '\n'.join([`x` for x in range(len(l))])

def _setSetting(setting: str):
	print(f'SET : {setting}')

	val = _confirmPolling()

	print(f'CONFIRM : {setting}')

	return val

def _confirmPolling():
	VAL = _get_coordinates()

	while REPEAT_VAL > 0:
		time.sleep(.5)
		TMP = _get_coordinates()
		print(TMP)

		if VAL == TMP:
			REPEAT_VAL -= 1
		else:
			REPEAT_VAL = REPEAT_MAX

	return VAL

def configureScreenFinder():
	return

def configure():
	output = []

	output.append(HEADER)
	for setting in SETTINGS:
		output_list.append(_setSetting(setting))

	output.append(FOOTER)

	output = _string_comprehension(output)
	write_file('_settings.py')

