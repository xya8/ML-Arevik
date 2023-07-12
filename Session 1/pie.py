import matplotlib.pyplot as plt

cat=["A", "B", "c","D"]
proc = [25, 30, 15, 30]
explode = [0, 0.1, 0 ,0]
colors = ["#421855", "#f59fe8", "black", "yellow"]

plt.pie(proc, explode = explode, labels = cat, colors=colors, shadow = True)
plt.title("Percentage Division")
plt.legend(cat)
plt.show()    
