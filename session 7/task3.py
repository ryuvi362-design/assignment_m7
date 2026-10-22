import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
zomato = [8, 10, 7, 12, 9, 11]
swiggy = [6, 9, 8, 10, 7, 13]
dominos = [3, 4, 5, 2, 6, 4]

fig, axs = plt.subplots(1, 3, figsize=(14, 4), sharey=True)

axs[0].bar(months, zomato, color='red')
axs[0].set_title('Zomato')
axs[0].set_ylabel('Number of Orders')

axs[1].bar(months, swiggy, color='orange')
axs[1].set_title('Swiggy')

axs[2].bar(months, dominos, color='blue')
axs[2].set_title("Domino's")

fig.suptitle('Food Orders Over the Last 6 Months')
plt.tight_layout()
plt.show()