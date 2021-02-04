from karel import *

def turn_right():
	turn_left()
	turn_left()
	turn_left()
def walk_to_cross_wall():
	turn_left()
	move()
	turn_right()
	while front_is_clear():
		move()
def place_beepers_sw():
#putting beepers in southwestern quadrant
	if not front_is_clear():
		turn_left()
		while facing_north():
			while not right_is_clear():
				put_beeper()
				move()
				if not front_is_clear():
					if facing_north():
						turn_left()
def turn_west_corner():
#turning around the westernmost wall
	turn_right()
	move()
	turn_right()
	move()
	
def place_beepers_nw():
#putting beepers in northwestern quadrant
	while facing_east():
		while not right_is_clear():
			put_beeper()
			move()
			if not front_is_clear():
				if facing_east():
					turn_left()
def turn_north_corner():
#turning around the northernmost wall
		turn_right()
		move()
		turn_right()
		move()
def place_beepers_ne():
#putting beepers in northeastern quadrant
	while facing_south():
		while not right_is_clear():
			put_beeper()
			move()
			if not front_is_clear():
				if facing_south():
					turn_left()
def turn_east_corner():
#turning around the easternmost wall
		turn_right()
		move()
		turn_right()
		move()
def place_beepers_se():
#putting beepers in southeastern quadrant
	while facing_west():
		while not right_is_clear():
			put_beeper()
			move()
			if not front_is_clear():
				if facing_west():
					turn_left()

begin_karel_program()

walk_to_cross_wall()
place_beepers_sw()
turn_west_corner()
place_beepers_nw()
turn_north_corner()
place_beepers_ne()
turn_east_corner()
place_beepers_se()

end_karel_program()