import stddraw
#graphics module
#head
def head():
    stddraw.circle(.75, .75, .08)
    stddraw.show(0)
#torso
def torso():
    stddraw.line(.75,.67, .75, .37)
    stddraw.show(0)
#left arm
def left_arm():
    stddraw.line(.75, .65, .7, .5)
    stddraw.show(0)
#right arm
def right_arm():
    stddraw.line(.75,.65, .8, .5)
    stddraw.show(0)
#left leg
def left_leg():
    stddraw.line(.75, .37, .7, .3)
    stddraw.show(0)
#right leg
def right_leg():
    stddraw.line(.75,.37, .8, .3)
    stddraw.show(0)
#gallows
def gallows():
    stddraw.line(.75, .83, .75,.9)
    stddraw.line(.75,.9,.9,.9)
    stddraw.line(.9,.9,.9,.2)
    stddraw.line(.55,.2,.95,.2)
    stddraw.line(.55,.2,.55,.1)
    stddraw.line(.95,.2,.95,.1)
    stddraw.line(.55,.1,.95,.1)
    stddraw.show(0)
#face
def face():
    stddraw.setFontSize(32)
    stddraw.text(.71,.75,"x")
    stddraw.text(.79,.75, "x")
    stddraw.text(.75,.70,"^")
    stddraw.show(1000)
#dashed letters
#wrong letter counters
def wrong():
    stddraw.setFontSize(30)
    stddraw.text(.25,.2,"Incorrect letters:")
    stddraw.show(1000)
def wrong_letters(bad_guesses):
    stddraw.setFontSize(28)
    for i in range(len(bad_guesses)):
        stddraw.text(0.07+ i * 0.03 ,.15, bad_guesses[i])
    stddraw.show(1000)
def word(reveal):
    stddraw.setFontSize(35)
    for i in range(len(reveal)):
        stddraw.text(.1+i * 0.03 ,.5,"".join(reveal[i]))
    stddraw.show(1000)
def win():
    stddraw.clear()
    stddraw.setFontSize(60)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.text(.5,.5, "YOU WIN!!")
    stddraw.show(5000)

def lose():
    stddraw.clear()
    stddraw.setFontSize(60)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(.5,.6, "YOU LOSE")
    stddraw.text(.5,.4, "GAME OVER")
    stddraw.show(5000)