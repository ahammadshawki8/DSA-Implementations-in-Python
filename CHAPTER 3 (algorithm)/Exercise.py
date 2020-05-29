import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")

x=np.arange(1,50,0.1)
y1=np.ones_like(x)
y2=np.log2(x) 
y3=x
y4=x*np.log2(x)
y5=x**2
y6=x**3
y7=2**x

plt.plot(x,y1,label=("Constant"))
plt.plot(x,y2,label=("Logarithm"))
plt.plot(x,y3,label=("Linear"))
plt.plot(x,y4,label=("N log N"))
plt.plot(x,y5,label=("Quadratic"))
plt.plot(x,y6,label=("Cubic"))
plt.plot(x,y7,label=("Exponential"))

plt.title("Different Time Complexity")
plt.legend()

plt.savefig("DTC.png")
plt.show()

