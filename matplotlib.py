import matplotlib.pyplot as plt

# 101 points: 0, 0.01, 0.02... 0.99, 1
xs = np.linspace(0, 1, 101)
# sine and cosine are evaluated at each of those points
fs = np.sin(2*np.pi*xs)
gs = np.cos(2*np.pi*xs)

plt.figure(figsize=(10,5))
# the graph of the sine is a dotted blue line
# the graph of the cosine is a solid green line
plt.plot(xs, fs, "b.", label="graph of f")
plt.plot(xs, gs, "g-", label="graph of g")
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("A graph that combines two plots")
