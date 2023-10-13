import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
x = np.linspace(1,10,120)
whitel=np.linspace(1,4,6)
morderatel=np.linspace(2,4,6)
blackl=np.linspace(2,8,6)
wm=np.mean(whitel)
mm=np.mean(morderatel)
bm=np.mean(blackl)
ws=np.std(whitel)
ms=np.std(morderatel)
bs=np.std(blackl)
white = fuzz.gaussmf(x,wm,ws)
moderate= fuzz.gaussmf(x,mm,ms)
black = fuzz.gaussmf(x,bm,bs)


plt.plot(x,white,label='white')
plt.plot(x,moderate,label='morderate')
plt.plot(x,black,label='black')
plt.show()
