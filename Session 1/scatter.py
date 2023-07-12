import matplotlib.pyplot as p
import random as r

r.seed(8)
x =[ r.random() for _ in range(50)]
y = [r.random() for _ in range(50)]
colors = [r.random() for _ in range(50)]
sizes = [r.random() for _ in range(50)]

p.scatter(x, y, c = colors, s = sizes, marker ="o")
p.xlabel("X")
p.ylabel("Y")
p.title("Scatter Plot")
p.grid(True)
p.show() 
