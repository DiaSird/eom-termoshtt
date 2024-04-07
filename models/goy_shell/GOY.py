import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("goy.csv").set_index("time")

df[["r4", "r8", "r16", "r26"]].plot()
plt.savefig("GOY.png")
plt.clf()

(df**2).mean().plot()
plt.yscale("log")
plt.savefig("error.png")
