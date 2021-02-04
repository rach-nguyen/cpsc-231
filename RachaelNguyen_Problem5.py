from karel import *
def turn_right():
	turn_left()
	turn_left()
	turn_left()
def turn_around():
	turn_left()
	turn_left()

def fill_row():
	even_or_odd()
def even_or_odd():
#determines whether karel places beepers on the even avenues or odd ones
	if facing_east():
		turn_right()
		if front_is_clear():
			move()
			if beepers_present():
				turn_around()
				move()
				turn_right()
				even()
			else:
				turn_around()
				move()
				turn_right()
				odd()
		else:
			turn_left()
			odd()
def odd():
#beepers on odd avenues
	put_beeper()
	while front_is_clear():
		move()
		if front_is_clear():
			move()
			put_beeper()
def even():
#beepers on even avenues
	while front_is_clear():
		move()
		if front_is_clear():
			put_beeper()
			move()
		else:
			put_beeper()
def back_to_west():
#go back to the western wall and has him face east
	if not front_is_clear():
		turn_around()
		while front_is_clear():
			move()
		turn_around()
def move_to_next_street():
#move up a street
	if facing_east():
		turn_left()
		if front_is_clear():
			move()
			turn_right()
		

begin_karel_program()
while facing_east():
	fill_row()
	back_to_west()
	move_to_next_street()
end_karel_program()