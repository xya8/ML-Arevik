import matplotlib.pyplot as plt

years = [10, 12, 14, 16, 18, 20]
population = [8, 9, 9, 10, 11, 11]

plt.plot(years, population, marker = "o", linestyle = "--", color = "#421855") 
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth")
plt.show()
