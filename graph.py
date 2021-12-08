import socket
import selectors
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


b = pd.read_csv("data.csv", usecols=[3])
with open("suppp.csv", "r") as f:
    a = f.read()
    a = a.replace(",", " ")
    a = a.split()

a = pd.DataFrame(a)




y2 = b.values
y1 = a.values
y1 = y1.astype(float)
print(type(y1))
ass = len(y1) / 2
ass2 = len(y2) / 2


x2 = np.arange(0, ass2, step=0.5)
x1 = np.arange(0, ass, step=0.5)

plt.plot(x2, y2, label="Real")
plt.plot(x1, y1, label="Predicted")

plt.legend()
plt.show()




