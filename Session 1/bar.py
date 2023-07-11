import matplotlib.pyplot  as plt 

products =["p1", "p2", "p3","p4"]
sales = [32, 24, 45, 52]

plt.bar(products, sales, color = ["red","blue","green", "orange"])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.legend(["Sales"])
plt.show() 
