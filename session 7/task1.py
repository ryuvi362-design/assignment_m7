import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
steps = [6500, 8200, 7100, 9000, 10500, 5800, 7600]
water = [2.0, 2.5, 3.0, 2.2, 3.5, 2.8, 3.0]

fig, axs = plt.subplots(2, 1, figsize=(8, 7))

axs[0].plot(days, steps, marker='o', color='green')
axs[0].set_title('Daily Step Count')
axs[0].set_ylabel('Steps')

axs[1].plot(days, water, marker='o', color='blue')
axs[1].set_title('Daily Water Intake')
axs[1].set_ylabel('Litres')

plt.tight_layout()
plt.show()