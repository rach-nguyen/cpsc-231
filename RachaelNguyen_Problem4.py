from karel import *
def turn_around():
	turn_left()
	turn_left()
	
def turn_right():
	turn_left()
	turn_left()
	turn_left()

def place_end_beepers():
	while front_is_clear():
		move()
		if not front_is_clear():
			if not beepers_present():
				put_beeper()
				turn_around()
		
def find_middle():
	if beepers_present():
		pick_beeper()
		turn_around()
		move()
		if not beepers_present():
			put_beeper()
		while front_is_clear():
			move()
			if beepers_present():
				pick_beeper()
				turn_around()
				move()
				if not beepers_present():
					put_beeper()

def go_to_middle():
	if not front_is_clear():
		turn_around()
		while not beepers_present():
			move()

begin_karel_program()
if front_is_clear():
	place_end_beepers()
	find_middle()
	go_to_middle()
	
else:
	put_beeper()
end_karel_program()