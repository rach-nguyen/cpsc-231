from p3 import GuitarString
import stdaudio
a_string = GuitarString(440.00)
b = a_string.pluck()
print(b)
c = a_string.tick()
print(c)
stdaudio.playSamples(100)