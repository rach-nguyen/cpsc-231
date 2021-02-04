import stddraw
import picture
import time
import sys
def configuration():
    stddraw.setCanvasSize(w=512,h=620)
    stddraw.setXscale(0,9)
    stddraw.setYscale(-9,0)
#taffies
#all images were found on google
def pika(x,y):
    stddraw.picture(picture.Picture("pika.jpg"),x,y)
def guy(x,y):
    stddraw.picture(picture.Picture("guy.jpg"),x,y)
def sonny(x,y):
    stddraw.picture(picture.Picture("sonny.jpg"),x,y)
def dog(x,y):
    stddraw.picture(picture.Picture("dog.jpg"),x,y)
def roblox(x,y):
    stddraw.picture(picture.Picture("roblox.png"),x,y)
def trash(x,y):
    stddraw.picture(picture.Picture("trash.jpg"),x,y)
def box(x,y):
    stddraw.setPenColor(stddraw.MAGENTA)
    stddraw.square(x,y,.5)
def clear_box(x,y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.square(x,y,.5)
def removed_taffy(x,y):
	stddraw.setPenColor(stddraw.WHITE)
	stddraw.filledSquare(x,y,.5)
def draw_clock(game_start):
    #https://introcs.cs.princeton.edu/python/15inout/clock.py.html
    current_time = time.time()
    time_elapsed = current_time - game_start - 5
    timer = '%02d:%02d'%(0,time_elapsed)
    stddraw.setFontSize(26)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(7.2,-1.2,2,1)
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.text(8.25,-.5,"TIME:")
    stddraw.text(8.25,-1, str(timer))
    stddraw.show(1)
    if time_elapsed >= 60:
        stddraw.clear()
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(36)
        stddraw.text(4.5,-4.5,"Time's up! Game over!")
        stddraw.show(1000)
        sys.exit()
def score(score):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(26)
    stddraw.filledRectangle(7.2,-2.5,2,1)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(8.25,-1.75,"SCORE:")
    stddraw.text(8.25,-2.25,str(score) + "/1000")

def goal():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(26)
    stddraw.filledRectangle(7.2,-3.75,2,1.3)
    stddraw.setPenColor(stddraw.ORANGE)
    stddraw.text(8.25,-3,"GOAL:")
    stddraw.setFontSize(16)
    stddraw.text(8,-3.5,"Score 1000 points")
    stddraw.text(8,-3.75, "within 1 minute!")
def win():
    stddraw.clear()
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontSize(36)
    stddraw.text(4.5,-4.5,"Congrats! You win!")
    stddraw.show(1000)
    sys.exit()