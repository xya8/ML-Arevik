import matplotlib.pyplot as p
import random

random.seed(42)
data = [random.normalvariate(0, 1) for _ in range(1000)]
p.hist(data, bins = 30, color = "skyblue", alpha = 0.7)
p.xlabel("Value")
p.ylabel("Fequency")
p.title("Frequency catch")
p.show()
