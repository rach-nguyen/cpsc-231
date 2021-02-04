import stdaudio, sys, random, math, stdstats, stddraw, stdarray

brown_v = stdarray.create1D(882000,0.0)

white = [random.uniform(-0.25,0.25) for i in range(882000)]

variance = 0.05
i = 0
i1 = 882000
f = 0.25
def fill_brownian(brown_v,i,i1,variance,scale):
#base condtion; when the differences between indexes = 1
# i.e. theyre next to each other
    if i1-i==1:
        return
    else:
        #find middle index
        mid_index = (i+i1) // 2
        #calculate midpoint value
        avg = (brown_v[i] + brown_v[i1])/2
        #add random number from normal distribution to midpoint value
        delta = random.gauss(0, math.sqrt(variance))
        mp = avg + delta
        #set new variance
        new_var = variance/scale
        #add to array
        brown_v[mid_index] = mp
        #call brownian before midpoint(inclusive)
        fill_brownian(brown_v,i, mid_index,new_var, scale)
        #after midpoint(exclusive)
        fill_brownian(brown_v,mid_index,i1,new_var, scale)

def brown():
    hurst_ex = 0.5
    scale = 2**(2*hurst_ex)
    fill_brownian(brown_v,0, 44100 ,variance, scale)
    fill_brownian(brown_v,44101,88200 ,variance, scale)       
    fill_brownian(brown_v,88201, 132300 ,variance, scale)
    fill_brownian(brown_v,132301, 176400 ,variance, scale)
    fill_brownian(brown_v,176401, 220500 ,variance, scale)
    fill_brownian(brown_v,220501, 264600 ,variance, scale)
    fill_brownian(brown_v,264601, 308700 ,variance, scale)
    fill_brownian(brown_v,308701, 352800 ,variance, scale)
    fill_brownian(brown_v,352801, 396900 ,variance, scale)
    fill_brownian(brown_v,396901, 441000 ,variance, scale)
    fill_brownian(brown_v,441001, 485100 ,variance, scale)
    fill_brownian(brown_v,485101, 529200 ,variance, scale)
    fill_brownian(brown_v,529201, 573300 ,variance, scale)
    fill_brownian(brown_v,573301, 617400 ,variance, scale)
    fill_brownian(brown_v,617401, 661500 ,variance, scale)
    fill_brownian(brown_v,661501, 705600 ,variance, scale)
    fill_brownian(brown_v,705601, 749700 ,variance, scale)
    fill_brownian(brown_v,749701, 793800 ,variance, scale)
    fill_brownian(brown_v,793801, 837900 ,variance, scale)
    fill_brownian(brown_v,837901, 881999 ,variance, scale)
def blend():
    blend = []
    for i in range(882000):
        t = i/44100
        s = (math.sin(math.pi*f*t))**6
        y = ((1-s)*brown_v[i]+s*white[i])
        blend.append(y)
        print(blend)
    stdaudio.playSamples(blend)
    stdaudio.wait()

if __name__=='__main__':
    brown()
    blend()
