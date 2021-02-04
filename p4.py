import stdaudio
import stddraw

from picture import Picture
from p3 import GuitarString

notes = ['q','2','w','e','4','r','5','t','y','7','u','8','i','9','o','p','-','[','=','z','x','d','c','f','v','g','b','n','j','m','k',',','.',';','/',"'",' ']
def multiplier(key,notes):
    for index, num in enumerate(notes):
        if num == key:
            return index
  

def frequency(num):
    freq = 110.00 * 2 ** (num/12) 
    return freq

play = GuitarString(110.00)

p = Picture('piano.png')
stddraw.picture(p)
stddraw.show(0.0)

escape = False
while not escape:
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        freq = frequency(multiplier(key,notes))
        play = GuitarString(freq)
        play.pluck()

    y = play.tick()
    stdaudio.playSample(y)
    
